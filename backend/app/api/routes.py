from fastapi import APIRouter

from app.services.market_data_service import MarketDataService
from app.services.price_alert_service import PriceAlertService
from app.analysis.technical import (
    sma,
    ema,
    rsi,
    macd,
    trend_signal,
)

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


@router.get("/technical/{symbol}")
def technical_analysis(symbol: str):
    history = market_data_service.get_history(symbol)

    prices = [
        item.close_price
        for item in history
        if item.close_price is not None
    ]

    if not prices:
        return {
            "symbol": symbol,
            "sma": [],
            "ema": [],
            "rsi": [],
            "macd": {
                "macd": [],
                "signal": [],
                "histogram": [],
            },
            "trend": "N/A",
        }

    sma_values = sma(prices, 20)
    ema_values = ema(prices, 20)
    rsi_values = rsi(prices)
    macd_values = macd(prices)

    latest_sma = sma_values[-1] if sma_values else None
    latest_ema = ema_values[-1] if ema_values else None
    latest_rsi = rsi_values[-1] if rsi_values else None
    latest_macd = (
        macd_values["macd"][-1]
        if macd_values["macd"]
        else None
    )
    latest_signal = (
        macd_values["signal"][-1]
        if macd_values["signal"]
        else None
    )

    trend = trend_signal(
        price=prices[-1],
        sma_value=latest_sma,
        ema_value=latest_ema,
        rsi_value=latest_rsi,
        macd_value=latest_macd,
        signal_value=latest_signal,
    )

    return {
        "symbol": symbol,
        "sma": sma_values,
        "ema": ema_values,
        "rsi": rsi_values,
        "macd": macd_values,
        "trend": trend,
    }


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
