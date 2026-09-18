from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["service"] == "user-service"
    assert data["status"] == "healthy"


def test_users():
    client = app.test_client()

    response = client.get("/users")

    assert response.status_code == 200

    data = response.get_json()

    assert data["service"] == "user-service"
    assert len(data["users"]) == 2

    assert data["users"][0]["id"] == 1
    assert data["users"][0]["name"] == "Pandu"

    assert data["users"][1]["id"] == 2
    assert data["users"][1]["name"] == "Alice"
