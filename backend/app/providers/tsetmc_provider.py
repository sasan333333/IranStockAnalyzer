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
