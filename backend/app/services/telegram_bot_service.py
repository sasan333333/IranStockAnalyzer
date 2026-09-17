class TelegramBotService:
    def __init__(self, token: str):
        self.token = token

    def build_message(self, text: str) -> str:
        return text
