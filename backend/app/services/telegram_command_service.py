class TelegramCommandService:
    def handle(self, command: str) -> str:
        if command == "/start":
            return "IranStockAnalyzer Bot"

        if command == "/help":
            return "Commands: /start, /help, /market"

        return "Unknown command"
