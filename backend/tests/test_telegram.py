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
    assert response.json()["response"] == "Commands: /start, /help, /market, /chart"


def test_telegram_chart_command(monkeypatch):
    fake_history = [
        {
            "date": "2026-09-18",
            "open": 1000,
            "high": 1100,
            "low": 900,
            "close": 1050,
        }
    ]

    def fake_get_history(self, symbol):
        return fake_history

    monkeypatch.setattr(
        "app.services.market_data_service.MarketDataService.get_history",
        fake_get_history,
    )

    response = client.get("/telegram/command/%2Fchart%20NOURI")

    assert response.status_code == 200

    data = response.json()["response"]

    assert data["symbol"] == "NOURI"
    assert data["type"] == "market_history_chart"
    assert data["status"] == "requested"
    assert data["data"] == fake_history
