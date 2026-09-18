class TelegramChartService:
    def build_chart_request(self, symbol: str) -> dict:
        return {
            "symbol": symbol,
            "type": "market_history_chart",
            "status": "requested",
        }
