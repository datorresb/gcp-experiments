from fastapi.testclient import TestClient
from main import app

def test_health_check():
    with TestClient(app) as client:
        response = client.get("/api/health")
        assert response.status_code == 200