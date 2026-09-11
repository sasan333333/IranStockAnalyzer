from app.models.price_alert import PriceAlert
from app.services.telegram_service import TelegramService


class PriceAlertService:

    def __init__(self, bot_token: str | None = None, chat_id: str | None = None):
        self.telegram_service = (
            TelegramService(bot_token)
            if bot_token
            else None
        )
        self.chat_id = chat_id

    def check_alert(
        self,
        symbol: str,
        current_price: float,
        target_price: float,
        tolerance_percent: float = 3.0,
    ):
        alert = PriceAlert(
            symbol=symbol,
            target_price=target_price,
            tolerance_percent=tolerance_percent,
            current_price=current_price,
        )

        result = {
            "symbol": symbol,
            "current_price": current_price,
            "target_price": target_price,
            "tolerance_percent": tolerance_percent,
            "triggered": alert.is_triggered,
        }

        if alert.is_triggered and self.telegram_service and self.chat_id:
            message = (
                f"Price Alert\n"
                f"Symbol: {symbol}\n"
                f"Current Price: {current_price}\n"
                f"Target Price: {target_price}\n"
                f"Tolerance: {tolerance_percent}%"
            )

            self.telegram_service.send_message(
                chat_id=self.chat_id,
                text=message,
            )

        return result
