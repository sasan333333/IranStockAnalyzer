from app.models.price_alert import PriceAlert


class PriceAlertService:

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

        return {
            "symbol": symbol,
            "current_price": current_price,
            "target_price": target_price,
            "tolerance_percent": tolerance_percent,
            "triggered": alert.is_triggered,
        }
