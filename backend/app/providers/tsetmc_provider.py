import requests


class TSETMCProvider:

    BASE_URL = "https://cdn.tsetmc.com/api"

    HEADERS = {
        "User-Agent": "Mozilla/5.0"
    }

    def get_instrument_code(self, symbol: str):
        response = requests.get(
            f"{self.BASE_URL}/Instrument/GetInstrumentSearch/{symbol}",
            headers=self.HEADERS,
            timeout=20
        )
        response.raise_for_status()

        data = response.json()
        results = data.get("instrumentSearch", [])

        if not results:
            return None

        return results[0].get("insCode")

    def get_market_data(self, symbol: str):
        ins_code = self.get_instrument_code(symbol)

        if not ins_code:
            raise ValueError("Symbol not found")

        response = requests.get(
            f"{self.BASE_URL}/ClosingPrice/GetClosingPriceInfo/{ins_code}",
            headers=self.HEADERS,
            timeout=20
        )
        response.raise_for_status()

        data = response.json().get("closingPriceInfo", {})

        return {
            "symbol": symbol,
            "last_price": data.get("pDrCotVal"),
            "close_price": data.get("pClosing"),
            "volume": data.get("qTotTran5J"),
        }

    def get_history(self, symbol: str):
        ins_code = self.get_instrument_code(symbol)

        if not ins_code:
            raise ValueError("Symbol not found")

        response = requests.get(
            f"{self.BASE_URL}/ClosingPrice/GetClosingPriceDailyList/{ins_code}/0",
            headers=self.HEADERS,
            timeout=30
        )
        response.raise_for_status()

        data = response.json()

        return data.get("closingPriceDaily", [])
