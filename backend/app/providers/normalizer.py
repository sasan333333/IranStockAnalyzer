from app.models.market_data import MarketData


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
