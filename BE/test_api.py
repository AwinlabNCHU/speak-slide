import requests
import json
import time
from datetime import datetime
import os
import subprocess
import signal
import psutil

BASE_URL = "http://localhost:8000/api/v1"
TEST_USER = {
    "email": "test@example.com",
    "username": "testuser",
    "password": "Test123!@#",
    "full_name": "Test User",
    "is_active": True,
}


def print_section(title):
    """Print a section header."""
    print(f"\n{'='*20} {title} {'='*20}")


def print_response(response, title="Response"):
    """Print response details."""
    print(f"\n{title}:")
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {dict(response.headers)}")
    try:
        print(f"Body: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"Raw Response: {response.text}")


def find_uvicorn_process():
    """Find the uvicorn server process."""
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            if "uvicorn" in " ".join(proc.info["cmdline"] or []):
                return proc
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return None


def kill_process_on_port(port=8000):
    """Kill any process using the specified port."""
    for proc in psutil.process_iter(["pid", "name", "connections"]):
        try:
            for conn in proc.connections():
                if conn.laddr.port == port:
                    print(f"Killing process {proc.pid} using port {port}")
                    proc.terminate()
                    proc.wait(timeout=5)
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
            pass
    return False


def restart_server():
    """Restart the FastAPI server."""
    print("\nRestarting FastAPI server...")

    # Find and kill existing server
    server = find_uvicorn_process()
    if server:
        try:
            print(f"Stopping existing server (PID: {server.pid})")
            server.terminate()
            server.wait(timeout=5)
        except psutil.TimeoutExpired:
            print("Server didn't stop gracefully, forcing kill")
            server.kill()
        except Exception as e:
            print(f"Error stopping server: {str(e)}")

    # Ensure port is free
    if kill_process_on_port():
        print("Freed port 8000")
        time.sleep(1)  # Give the OS time to release the port

    # Start new server
    try:
        print("Starting new server...")
        subprocess.Popen(
            ["uvicorn", "app.main:app", "--reload"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Wait for server to start
        max_retries = 5
        for i in range(max_retries):
            try:
                response = requests.get(f"{BASE_URL}/health", timeout=5)
                if response.status_code == 200:
                    print("Server is ready")
                    return True
            except requests.exceptions.ConnectionError:
                if i < max_retries - 1:
                    print(
                        f"Waiting for server to start (attempt {i + 1}/{max_retries})"
                    )
                    time.sleep(2)
                continue
        print("Server failed to start")
        return False
    except Exception as e:
        print(f"Error starting server: {str(e)}")
        return False


def cleanup_test_user():
    """Clean up test user if exists."""
    print("\n==================== Cleanup ====================")
    try:
        # Check if test user exists
        response = requests.get(
            f"{BASE_URL}/auth/debug/user/{TEST_USER['email']}", timeout=5
        )

        if response.status_code == 200:
            print("Test user exists, cleaning up...")
            # Delete database files
            db_files = ["vute.db", "sql_app.db"]
            for db_file in db_files:
                if os.path.exists(db_file):
                    try:
                        os.remove(db_file)
                        print(f"Deleted {db_file}")
                    except Exception as e:
                        print(f"Error deleting {db_file}: {str(e)}")

            # Recreate database
            try:
                result = subprocess.run(
                    ["python", "recreate_db.py"],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                if result.returncode == 0:
                    print("Database recreated successfully")

                    # Restart server to ensure fresh connection
                    if not restart_server():
                        print("Failed to restart server")
                        return False

                    # Give the server time to initialize
                    time.sleep(2)
                else:
                    print(f"Error recreating database: {result.stderr}")
                    return False
            except subprocess.TimeoutExpired:
                print("Database recreation timed out")
                return False
            except Exception as e:
                print(f"Error during database recreation: {str(e)}")
                return False

            # Verify user is gone
            response = requests.get(
                f"{BASE_URL}/auth/debug/user/{TEST_USER['email']}", timeout=5
            )
            if response.status_code == 404:
                print("Test user successfully removed")
                return True
            else:
                print("Test user still exists after cleanup")
                return False
        else:
            print("No test user found, proceeding with tests")
            return True

    except Exception as e:
        print(f"Error during cleanup: {str(e)}")
        return False


def test_health_check():
    print_section("Health Check")
    try:
        response = requests.get("http://localhost:8000/health")
        print_response(response, "Health Check Response")
        assert response.status_code == 200
    except Exception as e:
        print(f"Error: {str(e)}")
        assert False


def test_user_registration():
    print_section("User Registration")
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json=TEST_USER,
            headers={"Content-Type": "application/json"},
        )
        print_response(response, "Registration Response")
        assert response.status_code == 200 or response.status_code == 400
    except Exception as e:
        print(f"Error: {str(e)}")
        assert False


def test_user_login():
    """Test user login endpoint."""
    print_section("User Login")
    try:
        response = requests.post(
            f"{BASE_URL}/auth/login",
            data={"username": TEST_USER["email"], "password": TEST_USER["password"]},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        print_response(response, "Login Response")
        if response.status_code == 200:
            return response.json().get("access_token")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def test_debug_user():
    print_section("Debug User")
    try:
        response = requests.get(f"{BASE_URL}/auth/debug/user/{TEST_USER['email']}")
        print_response(response, "Debug User Response")
        assert response.status_code == 200
    except Exception as e:
        print(f"Error: {str(e)}")
        assert False


def test_forgot_password():
    print_section("Forgot Password")
    try:
        response = requests.post(
            f"{BASE_URL}/auth/forgot-password",
            json={"email": TEST_USER["email"]},
            headers={"Content-Type": "application/json"},
        )
        print_response(response, "Forgot Password Response")
        assert response.status_code in [200, 404]
    except Exception as e:
        print(f"Error: {str(e)}")
        assert False


def test_reset_password(access_token):
    """Test reset password endpoint."""
    print("\n==================== Reset Password ====================")

    # Test reset password
    reset_data = {"current_password": "testpass123", "new_password": "newpass123"}

    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.post(
            f"{BASE_URL}/auth/reset-password",
            params=reset_data,  # Send as query parameters
            headers=headers,
            timeout=5,
        )

        print("\nReset Password Response:")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")
        print(f"Body: {response.text}")

        if response.status_code == 200:
            print("Password reset successful!")
            return True
        else:
            print("Reset password failed. Stopping tests.")
            return False

    except Exception as e:
        print(f"Error during reset password test: {str(e)}")
        return False


def test_invalid_registration():
    print_section("Invalid Registration Tests")
    # Missing required field
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={"username": "testuser", "password": "Test123!@#", "full_name": "Test User", "is_active": True},
        headers={"Content-Type": "application/json"},
    )
    print_response(response, "Missing Required Field Response")
    assert response.status_code == 422
    # Invalid email
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={"email": "invalid-email", "username": "testuser", "password": "Test123!@#", "full_name": "Test User", "is_active": True},
        headers={"Content-Type": "application/json"},
    )
    print_response(response, "Invalid Email Response")
    assert response.status_code == 422
    # Short password
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={"email": "test2@example.com", "username": "testuser2", "password": "short", "full_name": "Test User", "is_active": True},
        headers={"Content-Type": "application/json"},
    )
    print_response(response, "Short Password Response")
    assert response.status_code == 422
    # Short username
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={"email": "test3@example.com", "username": "ab", "password": "Test123!@#", "full_name": "Test User", "is_active": True},
        headers={"Content-Type": "application/json"},
    )
    print_response(response, "Short Username Response")
    assert response.status_code == 422


def test_invalid_login():
    print_section("Invalid Login Tests")
    # Wrong password
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": TEST_USER["email"], "password": "wrongpassword"},
        headers={"Content-Type": "application/json"},
    )
    print_response(response, "Wrong Password Response")
    assert response.status_code == 401
    # Non-existent user
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "nonexistent@example.com", "password": "anypassword"},
        headers={"Content-Type": "application/json"},
    )
    print_response(response, "Non-existent User Response")
    assert response.status_code == 401


def run_all_tests():
    """Run all API tests."""
    print(f"\nStarting API Tests at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Clean up any existing test user
    if not cleanup_test_user():
        print("Cleanup failed. Stopping tests.")
        return

    # Run tests in sequence
    if not test_user_registration():
        return

    if not test_debug_user():
        return

    if not test_user_login():
        return

    if not test_forgot_password():
        return

    # Comment out or remove test_reset_password if access_token fixture is not defined
    # if not test_reset_password(access_token):
    #     return

    print("\nAll tests completed successfully!")


if __name__ == "__main__":
    run_all_tests()
