import requests
from urllib.parse import quote


BASE_URL = "https://cdn.tsetmc.com/api"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


class TSETMCProvider:

    def __init__(self, timeout=20):
        self.timeout = timeout

    def _get(self, url):
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=self.timeout
        )

        response.raise_for_status()

        return response.json()

    def search_symbol(self, symbol: str):
        url = (
            f"{BASE_URL}/Instrument/GetInstrumentSearch/"
            f"{quote(symbol)}"
        )

        data = self._get(url)

        return data.get("instrumentSearch", [])

    def get_history(self, ins_code: str, top: int = 0):
        url = (
            f"{BASE_URL}/ClosingPrice/"
            f"GetClosingPriceDailyList/"
            f"{ins_code}/{top}"
        )

        data = self._get(url)

        return data.get("closingPriceDaily", [])

    def get_quote(self, ins_code: str):
        url = (
            f"{BASE_URL}/ClosingPrice/"
            f"GetClosingPriceInfo/"
            f"{ins_code}"
        )

        return self._get(url)

    def get_client_type(self, ins_code: str):
        url = (
            f"{BASE_URL}/ClientType/"
            f"GetClientType/{ins_code}/1/0"
        )

        return self._get(url)
