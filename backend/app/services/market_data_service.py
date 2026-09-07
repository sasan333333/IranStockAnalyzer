from typing import List

from app.models.market_data import DailyMarketData
from app.providers.tsetmc import TSETMCProvider
from app.providers.normalizer import normalize_daily_data


class MarketDataService:
    """
    Service layer for retrieving and normalizing market data.

    Higher-level components such as FastAPI, Android API
    and Telegram should use this service instead of
    accessing the TSETMC provider directly.
    """

    def __init__(self):
        self.provider = TSETMCProvider()

    def get_daily_data(self, symbol: str) -> List[DailyMarketData]:
        """
        Fetch raw daily market data from TSETMC,
        then normalize it into DailyMarketData models.
        """

        raw_data = self.provider.get_daily_data(symbol)

        return normalize_daily_data(raw_data)
