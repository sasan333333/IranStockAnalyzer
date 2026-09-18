from app.services.market_data_service import MarketDataService


class TelegramChartService:
    def __init__(self):
        self.market_data_service = MarketDataService()

    def build_chart_request(self, symbol: str) -> dict:
        history = self.market_data_service.get_market_history(symbol)

        return {
            "symbol": symbol,
            "type": "market_history_chart",
            "status": "requested",
            "data": history,
        }
