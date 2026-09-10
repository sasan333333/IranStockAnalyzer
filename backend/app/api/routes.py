from fastapi import APIRouter

from app.services.market_data_service import MarketDataService

router = APIRouter()
market_data_service = MarketDataService()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/market-data")
def market_data():
    data = market_data_service.get_market_data()

    return {
        "symbol": data.symbol,
        "last_price": data.last_price,
        "close_price": data.close_price,
        "volume": data.volume,
    }
