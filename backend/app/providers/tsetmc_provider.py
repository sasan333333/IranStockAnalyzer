import requests


class TSETMCProvider:

    BASE_URL = "https://cdn.tsetmc.com/api"

    HEADERS = {
        "User-Agent": "Mozilla/5.0"
    }

    def _get(self, endpoint: str):
        response = requests.get(
            f"{self.BASE_URL}/{endpoint}",
            headers=self.HEADERS,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()

    def get_instrument_code(self, symbol: str):
        data = self._get(
            f"Instrument/GetInstrumentSearch/{symbol}"
        )

        results = data.get("instrumentSearch", [])

        if not results:
            return None

        return results[0].get("insCode")

    def get_market_data(self, symbol: str):
        ins_code = self.get_instrument_code(symbol)

        if not ins_code:
            raise ValueError("Symbol not found")

        data = self._get(
            f"ClosingPrice/GetClosingPriceInfo/{ins_code}"
        )

        info = data.get("closingPriceInfo", {})

        return {
            "symbol": symbol,
            "last_price": info.get("pDrCotVal"),
            "close_price": info.get("pClosing"),
            "volume": info.get("qTotTran5J"),
        }

    def get_history(self, symbol: str):
        ins_code = self.get_instrument_code(symbol)

        if not ins_code:
            raise ValueError("Symbol not found")

        data = self._get(
            f"ClosingPrice/GetClosingPriceDailyList/{ins_code}/0"
        )

        return data.get("closingPriceDaily", [])
