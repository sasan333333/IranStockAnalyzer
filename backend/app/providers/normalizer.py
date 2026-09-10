from app.models.market_data import MarketData


def normalize_market_data(raw_data):
    return MarketData(
        symbol=raw_data.get("symbol"),
        last_price=raw_data.get("last_price"),
        close_price=raw_data.get("close_price"),
        volume=raw_data.get("volume"),
    )
