from app.services.market_scanner_service import MarketScannerService


def test_market_scanner():
    service = MarketScannerService()

    class FakeData:
        symbol = "NOURI"
        last_price = 1000
        close_price = 990
        volume = 50000

    service.market_data_service.get_market_data = lambda symbol: FakeData()

    result = service.scan(["NOURI"])

    assert result == [
        {
            "symbol": "NOURI",
            "last_price": 1000,
            "close_price": 990,
            "volume": 50000,
        }
    ]
