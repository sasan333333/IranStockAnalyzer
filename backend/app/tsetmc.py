import requests


BASE_URL = "https://cdn.tsetmc.com/api"


def search_symbol(symbol: str):
    """
    Search for a symbol in TSETMC.
    Example: فملی
    """
    url = f"{BASE_URL}/Instrument/GetInstrumentSearch/{symbol}"

    response = requests.get(
        url,
        timeout=15,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    return response.json()


def get_history(ins_code: str):
    """
    Get daily chart history for a symbol using its TSETMC InsCode.
    """
    url = f"{BASE_URL}/ClosingPrice/GetChartData/{ins_code}/D"

    response = requests.get(
        url,
        timeout=15,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    result = search_symbol("فملی")

    print("Search result:")
    print(result)
