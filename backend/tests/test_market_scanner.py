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

    def filter_volume(
        self,
        results: list[dict],
        minimum_volume: int,
    ) -> list[dict]:
        return [
            result
            for result in results
            if result["volume"] >= minimum_volume
        ]

    def filter_price_change(
        self,
        results: list[dict],
        minimum_change_percent: float,
    ) -> list[dict]:
        filtered = []

        for result in results:
            close_price = result["close_price"]
            last_price = result["last_price"]

            if close_price == 0:
                continue

            change_percent = (
                (last_price - close_price) / close_price
            ) * 100

            if change_percent >= minimum_change_percent:
                result = result.copy()
                result["price_change_percent"] = change_percent
                filtered.append(result)

        return filtered
