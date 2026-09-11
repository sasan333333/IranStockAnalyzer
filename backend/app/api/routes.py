from fastapi import APIRouter

from app.services.market_data_service import MarketDataService
from app.services.price_alert_service import PriceAlertService

router = APIRouter()
market_data_service = MarketDataService()
price_alert_service = PriceAlertService()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/market-data/{symbol}")
def market_data(symbol: str):
    data = market_data_service.get_market_data(symbol)

    return {
        "symbol": data.symbol,
        "last_price": data.last_price,
        "close_price": data.close_price,
        "volume": data.volume,
    }


@router.get("/market-history/{symbol}")
def market_history(symbol: str):
    history = market_data_service.get_history(symbol)

    return [
        {
            "date": item.date,
            "open_price": item.open_price,
            "high_price": item.high_price,
            "low_price": item.low_price,
            "close_price": item.close_price,
            "volume": item.volume,
        }
        for item in history
    ]


@router.get("/price-alert/{symbol}")
def price_alert(
    symbol: str,
    current_price: float,
    target_price: float,
    tolerance_percent: float = 3.0,
):
    return price_alert_service.check_alert(
        symbol=symbol,
        current_price=current_price,
        target_price=target_price,
        tolerance_percent=tolerance_percent,
    )
