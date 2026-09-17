from fastapi import APIRouter

router = APIRouter()


@router.get("/telegram/health")
def telegram_health():
    return {"status": "ok"}
