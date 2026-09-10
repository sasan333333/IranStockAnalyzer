from dataclasses import dataclass
from typing import Optional


@dataclass
class MarketData:
    symbol: str
    last_price: Optional[float] = None
    close_price: Optional[float] = None
    volume: Optional[int] = None
