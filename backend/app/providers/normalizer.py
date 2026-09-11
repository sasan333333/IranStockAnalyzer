from app.models.market_data import MarketData
from app.models.market_history import MarketHistory


def normalize_market_data(raw_data):
    return MarketData(
        symbol=raw_data.get("symbol"),
        last_price=float(raw_data["last_price"])
        if raw_data.get("last_price") is not None else None,
        close_price=float(raw_data["close_price"])
        if raw_data.get("close_price") is not None else None,
        volume=int(raw_data["volume"])
        if raw_data.get("volume") is not None else None,
    )


def normalize_market_history(raw_history):
    result = []

    for item in raw_history:
        result.append(
            MarketHistory(
                date=str(item.get("dEven") or item.get("date")),
                open_price=item.get("pOpening"),
                high_price=item.get("pHigh"),
                low_price=item.get("pLow"),
                close_price=item.get("pClosing"),
                volume=item.get("qTotTran5J"),
            )
        )

    return result
