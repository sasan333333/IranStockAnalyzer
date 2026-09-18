import os

import requests


class TelegramDeliveryService:

    def __init__(self):
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    def send_chart(self, chart_data: dict) -> dict:
        if not self.bot_token:
            return {
                "status": "ready",
                "type": "telegram_chart",
                "symbol": chart_data["symbol"],
                "data": chart_data,
            }

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

        response = requests.post(
            url,
            json={
                "chat_id": chart_data.get("chat_id"),
                "text": self._build_message(chart_data),
            },
            timeout=15,
        )

        response.raise_for_status()

        return {
            "status": "sent",
            "type": "telegram_chart",
            "symbol": chart_data["symbol"],
            "data": chart_data,
        }

    def _build_message(self, chart_data: dict) -> str:
        return (
            f"Symbol: {chart_data['symbol']}\n"
            f"Type: {chart_data['type']}\n"
            f"Status: {chart_data['status']}"
        )
