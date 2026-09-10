import requests


class TSETMCProvider:

    BASE_URL = "https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/"

    def get_market_data(self, symbol: str):
        response = requests.get(
            self.BASE_URL + symbol,
            timeout=20
        )
        response.raise_for_status()

        data = response.json()

        return {
            "symbol": symbol,
            "last_price": data.get("lastPrice"),
            "close_price": data.get("pClosing"),
            "volume": data.get("qTotTran5J"),
        }

    def get_history(self, symbol: str):
        return []
