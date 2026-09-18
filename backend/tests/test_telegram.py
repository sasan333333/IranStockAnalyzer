from fastapi.testclient import TestClient

from app.main import app
from app.services.telegram_delivery_service import TelegramDeliveryService


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
    assert data["type"] == "telegram_chart"
    assert data["status"] == "ready"
    assert data["data"]["type"] == "market_history_chart"
    assert data["data"]["data"] == fake_history


def test_telegram_delivery_service():
    service = TelegramDeliveryService()

    chart_data = {
        "symbol": "NOURI",
        "type": "market_history_chart",
        "status": "requested",
        "data": [],
    }

    result = service.send_chart(chart_data)

    assert result["status"] == "ready"
    assert result["type"] == "telegram_chart"
    assert result["data"] == chart_data
