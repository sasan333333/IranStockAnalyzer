from dataclasses import dataclass
from typing import Optional


@dataclass
class DailyMarketData:
    symbol: str
    name: str
    ins_code: str
    date: str

    open_price: Optional[float] = None
    high_price: Optional[float] = None
    low_price: Optional[float] = None
    close_price: Optional[float] = None
    last_price: Optional[float] = None
    yesterday_price: Optional[float] = None

    volume: Optional[int] = None
    value: Optional[float] = None
    trade_count: Optional[int] = None


@dataclass
class ClientTypeData:
    symbol: str
    ins_code: str
    date: str

    individual_buy_volume: Optional[int] = None
    legal_buy_volume: Optional[int] = None

    individual_sell_volume: Optional[int] = None
    legal_sell_volume: Optional[int] = None

    individual_buyer_count: Optional[int] = None
    legal_buyer_count: Optional[int] = None

    individual_seller_count: Optional[int] = None
    legal_seller_count: Optional[int] = None
