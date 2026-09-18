from fastapi.testclient import TestClient

from app.main import app
from app.services.market_scanner_service import MarketScannerService


client = TestClient(app)


def test_market_scanner_api(monkeypatch):
    class FakeData:
        symbol = "NOURI"
        last_price = 1100
        close_price = 1000
        volume = 50000

    def fake_get_market_data(self, symbol):
        return FakeData()

    monkeypatch.setattr(
        MarketScannerService.market_data_service.__class__,
        "get_market_data",
        fake_get_market_data,
    )

    response = client.post(
        "/market-scanner",
        json=["NOURI"],
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["data"][0]["symbol"] == "NOURI"
    assert data["data"][0]["last_price"] == 1100
    assert data["data"][0]["close_price"] == 1000
    assert data["data"][0]["volume"] == 50000
