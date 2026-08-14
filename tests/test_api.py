import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_unauthorized():
    """Verify that calling /predict without a token returns 401 Unauthorized."""
    response = client.post("/predict", json={"features": [1000, 2, 700]})
    assert response.status_code == 401

def test_login_success():
    """Verify login route returns a valid access token."""
    login_data = {"username": "admin", "password": "password"}
    response = client.post("/login", data=login_data)

    assert response.status_code == 200
    json_data = response.json()
    assert "access_token" in json_data
    assert json_data["token_type"] == "bearer"

def test_predict_invalid_payload():
    """Verify that sending an empty body returns a 422 Validation Error."""
    login_res = client.post("/login", data={"username": "admin", "password": "password"})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/predict", json={}, headers=headers)
    assert response.status_code == 422
