from fastapi import APIRouter

from app.services.market_data_service import MarketDataService

router = APIRouter()
market_data_service = MarketDataService()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/market-data")
def market_data():
    return market_data_service.get_market_data()
