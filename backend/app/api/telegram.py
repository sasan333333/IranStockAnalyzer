from fastapi import APIRouter

from app.services.market_data_service import MarketDataService
from app.services.telegram_command_service import TelegramCommandService

router = APIRouter()

command_service = TelegramCommandService()


@router.get("/telegram/health")
def telegram_health():
    return {"status": "ok"}


@router.get("/telegram/market-data/{symbol}")
def telegram_market_data(symbol: str):
    service = MarketDataService()
    return service.get_market_data(symbol)


@router.get("/telegram/command/{command}")
def telegram_command(command: str):
    return {
        "response": command_service.handle(command)
    }
