from fastapi import APIRouter

from app.services.market_data_service import MarketDataService

router = APIRouter()


@router.get("/telegram/health")
def telegram_health():
    return {"status": "ok"}


@router.get("/telegram/market-data/{symbol}")
def telegram_market_data(symbol: str):
    service = MarketDataService()
    return service.get_market_data(symbol)
