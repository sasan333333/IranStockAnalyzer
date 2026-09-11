from dataclasses import dataclass
from typing import Optional


@dataclass
class PriceAlert:
    symbol: str
    target_price: float
    tolerance_percent: float = 3.0
    current_price: Optional[float] = None

    @property
    def is_triggered(self) -> bool:
        if self.current_price is None:
            return False

        lower = self.target_price * (1 - self.tolerance_percent / 100)
        upper = self.target_price * (1 + self.tolerance_percent / 100)

        return lower <= self.current_price <= upper
