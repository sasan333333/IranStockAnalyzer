from app.services.market_data_service import MarketDataService
from app.services.telegram_delivery_service import TelegramDeliveryService


class TelegramChartService:
    def __init__(self):
        self.market_data_service = MarketDataService()
        self.delivery_service = TelegramDeliveryService()

    def build_chart_request(self, symbol: str) -> dict:
        history = self.market_data_service.get_history(symbol)

        chart_data = {
            "symbol": symbol,
            "type": "market_history_chart",
            "status": "requested",
            "data": history,
        }

        return self.delivery_service.send_chart(chart_data)
