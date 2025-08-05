import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello, FastAPI"}

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "pong"}

def test_connection():
    response = client.get("/connection")
    assert response.status_code == 200
    assert response.json() == {"status": "the backend is now available on port 1000"}
