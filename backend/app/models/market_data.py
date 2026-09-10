from dataclasses import dataclass
from typing import Optional


@dataclass
class MarketData:
    symbol: str
    last_price: Optional[float] = None
    close_price: Optional[float] = None
    volume: Optional[int] = None

    @property
    def price_change(self) -> Optional[float]:
        if self.last_price is None or self.close_price is None:
            return None

        return self.last_price - self.close_price

    @property
    def price_change_percent(self) -> Optional[float]:
        if self.close_price in (None, 0) or self.last_price is None:
            return None

        return ((self.last_price - self.close_price) / self.close_price) * 100
