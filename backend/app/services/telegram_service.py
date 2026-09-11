import requests


class TelegramService:

    BASE_URL = "https://api.telegram.org"

    def __init__(self, bot_token: str):
        self.bot_token = bot_token

    def send_message(self, chat_id: str, text: str):
        url = f"{self.BASE_URL}/bot{self.bot_token}/sendMessage"

        response = requests.post(
            url,
            data={
                "chat_id": chat_id,
                "text": text,
            },
            timeout=20,
        )

        response.raise_for_status()

        return response.json()

    def send_chart(self, chat_id: str, chart_path: str, caption: str = ""):
        url = f"{self.BASE_URL}/bot{self.bot_token}/sendPhoto"

        with open(chart_path, "rb") as chart:
            response = requests.post(
                url,
                data={
                    "chat_id": chat_id,
                    "caption": caption,
                },
                files={
                    "photo": chart,
                },
                timeout=30,
            )

        response.raise_for_status()

        return response.json()
