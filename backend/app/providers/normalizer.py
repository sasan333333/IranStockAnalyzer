from models.market_data import DailyMarketData
from models.tsetmc_mapper import map_daily_data


def normalize_history(
    raw_history: list,
    symbol: str,
    name: str,
    ins_code: str
) -> list[DailyMarketData]:

    normalized = []

    for raw_item in raw_history:
        item = map_daily_data(
            raw_data=raw_item,
            symbol=symbol,
            name=name,
            ins_code=ins_code
        )

        normalized.append(item)

    return normalized
