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
    return market_data_service.provider.get_history(symbol)
