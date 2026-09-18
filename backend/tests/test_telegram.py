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
    assert data["data"]["symbol"] == "NOURI"
    assert data["data"]["type"] == "market_history_chart"
    assert data["data"]["status"] == "requested"
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
    assert result["symbol"] == "NOURI"
    assert result["data"] == chart_data


def test_telegram_webhook():
    response = client.post(
        "/telegram/webhook",
        json={
            "message": {
                "text": "/start"
            }
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "processed"
    assert data["response"] == "IranStockAnalyzer Bot"


def test_telegram_webhook_empty_message():
    response = client.post(
        "/telegram/webhook",
        json={
            "message": {}
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ignored"
    assert data["response"] is None


def test_telegram_webhook_blank_message():
    response = client.post(
        "/telegram/webhook",
        json={
            "message": {
                "text": "   "
            }
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ignored"
    assert data["response"] is None


def test_telegram_webhook_unknown_command():
    response = client.post(
        "/telegram/webhook",
        json={
            "message": {
                "text": "   /unknown   "
            }
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "processed"
    assert data["response"] == "Unknown command"


def test_telegram_webhook_market_command(monkeypatch):
    class FakeMarketData:
        symbol = "NOURI"
        last_price = 1000
        close_price = 990
        volume = 50000

    def fake_get_market_data(self, symbol):
        return FakeMarketData()

    monkeypatch.setattr(
        "app.services.market_data_service.MarketDataService.get_market_data",
        fake_get_market_data,
    )

    response = client.post(
        "/telegram/webhook",
        json={
            "message": {
                "text": "/market NOURI"
            }
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "processed"
    assert "Symbol: NOURI" in data["response"]


def test_telegram_webhook_chart_command(monkeypatch):
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

    response = client.post(
        "/telegram/webhook",
        json={
            "message": {
                "text": "/chart NOURI"
            }
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "processed"
    assert data["response"]["symbol"] == "NOURI"
    assert data["response"]["type"] == "telegram_chart"
    assert data["response"]["status"] == "ready"
    assert data["response"]["data"]["data"] == fake_history
