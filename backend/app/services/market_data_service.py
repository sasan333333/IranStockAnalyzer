from app.providers.tsetmc_provider import TSETMCProvider
from app.providers.normalizer import normalize_market_data


class MarketDataService:

    def __init__(self):
        self.provider = TSETMCProvider()

    def get_market_data(self):
        raw_data = self.provider.get_market_data()
        return normalize_market_data(raw_data)
