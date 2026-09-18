class TelegramDeliveryService:
    def send_chart(self, chart_data: dict) -> dict:
        return {
            "symbol": chart_data["symbol"],
            "type": "telegram_chart",
            "status": "ready",
            "data": chart_data,
        }
