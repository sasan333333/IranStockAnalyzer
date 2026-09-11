from fastapi import APIRouter

from app.services.market_data_service import MarketDataService

router = APIRouter()
market_data_service = MarketDataService()


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
