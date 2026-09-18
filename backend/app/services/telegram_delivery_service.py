class TelegramDeliveryService:
    def send_chart(self, chart_data: dict) -> dict:
        return {
            "status": "ready",
            "type": "telegram_chart",
            "data": chart_data,
        }
