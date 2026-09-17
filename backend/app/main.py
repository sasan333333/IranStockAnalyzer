from fastapi import FastAPI

from app.api.routes import router as api_router
from app.api.telegram import router as telegram_router

app = FastAPI(title="IranStockAnalyzer")

app.include_router(api_router)
app.include_router(telegram_router)
