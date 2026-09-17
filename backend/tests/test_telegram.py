from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_telegram_health():
    response = client.get("/telegram/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_telegram_start_command():
    response = client.get("/telegram/command/%2Fstart")

    assert response.status_code == 200
    assert response.json()["response"] == "IranStockAnalyzer Bot"


def test_telegram_help_command():
    response = client.get("/telegram/command/%2Fhelp")

    assert response.status_code == 200
    assert "Commands:" in response.json()["response"]
