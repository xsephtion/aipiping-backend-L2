import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Piping Challenge" in response.text


def test_recommendation_valid():
    data = {"country": "Philippines", "season": "Summer"}
    response = client.post("/recommendation", data=json.dumps(data))
    assert response.status_code == 200
    result = response.json()
    assert result["country"] == "Philippines"
    assert result["season"] == "Summer"
    assert isinstance(result["recommendations"], list)


def test_recommendation_invalid_season():
    data = {"country": "Philippines", "season": "InvalidSeason"}
    response = client.post("/recommendation", data=json.dumps(data))
    assert response.status_code == 400
    assert "Invalid Season Selected" in response.text

# Add more test cases as needed
