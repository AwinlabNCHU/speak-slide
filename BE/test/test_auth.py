import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    # Register a new user
    register_data = {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "TestPassword123"
    }
    response = client.post("/api/v1/auth/register", json=register_data)
    assert response.status_code == 200 or response.status_code == 400  # 400 if already exists

    # Login with the new user
    login_data = {
        "email": "testuser@example.com",
        "password": "TestPassword123"
    }
    response = client.post("/api/v1/auth/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200