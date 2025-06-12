import requests
import json
import sys

def check_user_exists(email):
    """
    Check if a user exists with the given email.
    """
    url = f"http://localhost:8000/api/v1/auth/debug/user/{email}"
    try:
        response = requests.get(url)
        print(f"\nDebug - User Check Response:")
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        try:
            print(f"Response Body: {json.dumps(response.json(), indent=2)}")
        except:
            print(f"Raw Response: {response.text}")
        return response.json()
    except Exception as e:
        print(f"Error checking user: {str(e)}")
        return None

def register_user(email, username, password, full_name):
    """
    Register a new user with the provided details.
    """
    # API endpoint
    url = "http://localhost:8000/api/v1/auth/register"
    
    # User data
    user_data = {
        "email": email,
        "username": username,
        "password": password,
        "full_name": full_name,
        "is_active": True
    }
    
    # Headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        print("\nDebug - Registration Request:")
        print(f"URL: {url}")
        print(f"Headers: {headers}")
        print(f"Data: {json.dumps(user_data, indent=2)}")
        
        # Make the request
        response = requests.post(url, json=user_data, headers=headers)
        
        print("\nDebug - Registration Response:")
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        try:
            response_data = response.json()
            print(f"Response Body: {json.dumps(response_data, indent=2)}")
        except json.JSONDecodeError:
            print(f"Raw Response: {response.text}")
            print("Error: Could not parse JSON response")
            return None
        
        if response.status_code >= 400:
            print(f"Error: Server returned status code {response.status_code}")
            return None
            
        return response_data
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Is it running?")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {str(e)}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

def get_user_input():
    """
    Get user registration details with validation.
    """
    print("\n=== New User Registration ===")
    
    # Get email
    while True:
        email = input("Enter your email: ").strip()
        if '@' in email and '.' in email:
            break
        print("Please enter a valid email address.")
    
    # Get username
    while True:
        username = input("Enter your username (3-20 characters): ").strip()
        if 3 <= len(username) <= 20:
            break
        print("Username must be between 3 and 20 characters.")
    
    # Get password
    while True:
        password = input("Enter your password (min 8 characters): ").strip()
        if len(password) >= 8:
            break
        print("Password must be at least 8 characters long.")
    
    # Get full name
    while True:
        full_name = input("Enter your full name: ").strip()
        if full_name:
            break
        print("Full name cannot be empty.")
    
    return email, username, password, full_name

def check_server_status():
    """
    Check if the server is running and accessible.
    """
    try:
        response = requests.get("http://localhost:8000/health")
        return response.status_code == 200
    except:
        return False

def main():
    print("=== User Account Setup ===")
    
    # Check if server is running
    if not check_server_status():
        print("Error: Cannot connect to the server. Please make sure it's running at http://localhost:8000")
        sys.exit(1)
    
    # Get email to check
    email = input("Enter your email to check if you have an account: ").strip()
    
    # Check if user exists
    print("\nChecking if user exists...")
    user_check = check_user_exists(email)
    
    if user_check and user_check.get("exists"):
        print("\nUser already exists!")
        print("You can login using your email and password.")
        return
    
    print("\nNo existing account found.")
    proceed = input("Would you like to create a new account? (yes/no): ").lower()
    
    if proceed != 'yes':
        print("Account creation cancelled.")
        return
    
    # Get user details and register
    email, username, password, full_name = get_user_input()
    
    # Register the user
    result = register_user(email, username, password, full_name)
    
    if result:
        print("\nRegistration successful!")
        print("You can now login with your email and password.")
    else:
        print("\nRegistration failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 