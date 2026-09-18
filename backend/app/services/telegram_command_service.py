from app.services.market_data_service import MarketDataService


class TelegramCommandService:
    def __init__(self):
        self.market_data_service = MarketDataService()

    def handle(self, command: str) -> str:
        if command == "/start":
            return "IranStockAnalyzer Bot"

        if command == "/help":
            return "Commands: /start, /help, /market, /chart"

        if command.startswith("/market "):
            symbol = command.split(" ", 1)[1].strip()

            if not symbol:
                return "Symbol is required"

            data = self.market_data_service.get_market_data(symbol)

            return (
                f"Symbol: {data.symbol}\n"
                f"Last Price: {data.last_price}\n"
                f"Close Price: {data.close_price}\n"
                f"Volume: {data.volume}"
            )

        if command.startswith("/chart "):
            symbol = command.split(" ", 1)[1].strip()

            if not symbol:
                return "Symbol is required"

            return f"Chart requested for {symbol}"

        return "Unknown command"
