from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/market-data")
def market_data():
    return {
        "status": "ok",
        "message": "Market Data API ready"
    }
