from fastapi.testclient import TestClient

from tests.test_db import TestingSessionLocal
from app.main import app
from app.services.disc_service import DiscService
from app.api.v1.disc import get_disc_service

client = TestClient(app)


# Dependency to override the get_db dependency in the main app
def override_get_disc_service():
    session = TestingSessionLocal()
    yield DiscService(session=session)


app.dependency_overrides[get_disc_service] = override_get_disc_service


def test_create_and_get_disc():
    response = client.post("/api/v1/discs", json={"name": "Test Disc"})
    assert response.status_code == 200
    created_disc = response.json()
    assert created_disc["name"] == "Test Disc"
    assert "id" in created_disc

    # Fetch the same disc
    get_response = client.get(f"/api/v1/discs/{created_disc['id']}")
    assert get_response.status_code == 200
    fetched_disc = get_response.json()
    assert fetched_disc["id"] == created_disc["id"]
    assert fetched_disc["name"] == "Test Disc"
