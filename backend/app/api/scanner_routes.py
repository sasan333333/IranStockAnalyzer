from fastapi import APIRouter

from app.services.market_scanner_service import MarketScannerService


router = APIRouter()


@router.post("/market-scanner")
def market_scanner(symbols: list[str]):
    service = MarketScannerService()

    return {
        "status": "ok",
        "data": service.scan(symbols),
    }
