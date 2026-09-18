from fastapi import FastAPI

from app.api.routes import router
from app.api.telegram_routes import router as telegram_router
from app.api.scanner_routes import router as scanner_router


app = FastAPI(title="IranStockAnalyzer")

app.include_router(router)
app.include_router(telegram_router)
app.include_router(scanner_router)
