import requests
from urllib.parse import quote


BASE_URL = "https://cdn.tsetmc.com/api"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def search_symbol(symbol: str):
    url = f"{BASE_URL}/Instrument/GetInstrumentSearch/{quote(symbol)}"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    return data.get("instrumentSearch", [])


def get_history(ins_code: str):
    url = f"{BASE_URL}/ClosingPrice/GetClosingPriceDailyList/{ins_code}/0"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    return data.get("closingPriceDaily", [])


if __name__ == "__main__":

    symbol = "فملی"

    print(f"Searching for: {symbol}")

    results = search_symbol(symbol)

    if not results:
        print("Symbol not found.")
        exit(1)

    print("\nSearch results:")

    for item in results[:5]:
        print(
            item.get("lVal18AFC"),
            "|",
            item.get("lVal30"),
            "|",
            item.get("insCode")
        )

    instrument = results[0]

    ins_code = instrument["insCode"]

    print("\nSelected instrument:")
    print("Symbol:", instrument.get("lVal18AFC"))
    print("Name:", instrument.get("lVal30"))
    print("InsCode:", ins_code)

    history = get_history(ins_code)

    print("\nHistory records:", len(history))

    if history:
        print("\nFirst record:")
        print(history[0])
