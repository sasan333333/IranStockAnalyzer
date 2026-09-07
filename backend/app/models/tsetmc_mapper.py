from .market_data import DailyMarketData


def map_daily_data(
    raw_data: dict,
    symbol: str,
    name: str,
    ins_code: str
) -> DailyMarketData:

    return DailyMarketData(
        symbol=symbol,
        name=name,
        ins_code=ins_code,
        date=str(raw_data.get("dEven", "")),

        open_price=raw_data.get("priceFirst"),
        high_price=raw_data.get("priceMax"),
        low_price=raw_data.get("priceMin"),
        close_price=raw_data.get("pClosing"),
        last_price=raw_data.get("pDrCotVal"),
        yesterday_price=raw_data.get("priceYesterday"),

        volume=raw_data.get("qTotTran5J"),
        value=raw_data.get("qTotCap"),
        trade_count=raw_data.get("zTotTran")
    )
