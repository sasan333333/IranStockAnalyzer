from app.services.market_data_service import MarketDataService


class MarketScannerService:

    def __init__(self):
        self.market_data_service = MarketDataService()

    def scan(self, symbols: list[str]) -> list[dict]:
        results = []

        for symbol in symbols:
            data = self.market_data_service.get_market_data(symbol)

            results.append(
                {
                    "symbol": data.symbol,
                    "last_price": data.last_price,
                    "close_price": data.close_price,
                    "volume": data.volume,
                }
            )

        return results
