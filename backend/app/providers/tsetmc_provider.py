import requests


class TSETMCProvider:

    def get_market_data(self, symbol: str):
        return {
            "symbol": symbol,
            "last_price": None,
            "close_price": None,
            "volume": None,
        }
