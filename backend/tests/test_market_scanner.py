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


def test_filter_volume():
    service = MarketScannerService()

    results = [
        {"symbol": "NOURI", "volume": 50000},
        {"symbol": "FOLD", "volume": 10000},
    ]

    result = service.filter_volume(results, 20000)

    assert result == [
        {"symbol": "NOURI", "volume": 50000},
    ]


def test_filter_price_change():
    service = MarketScannerService()

    results = [
        {
            "symbol": "NOURI",
            "last_price": 1100,
            "close_price": 1000,
            "volume": 50000,
        },
        {
            "symbol": "FOLD",
            "last_price": 1020,
            "close_price": 1000,
            "volume": 30000,
        },
    ]

    result = service.filter_price_change(results, 5)

    assert len(result) == 1
    assert result[0]["symbol"] == "NOURI"
    assert result[0]["price_change_percent"] == 10
