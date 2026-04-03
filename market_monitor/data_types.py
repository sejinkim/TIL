from dataclasses import dataclass
from enum import Enum

class MarketStatus(str, Enum):
    OPEN = "장중"
    CLOSED = "장마감"
    PRE = "장전"

@dataclass
class PriceTick:
    symbol: str
    price:  int
    volume: int
    status: MarketStatus=MarketStatus.OPEN

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("가격은 0 이상이어야 합니다.")
        if self.volume < 0:
            raise ValueError("거래량은 0 이상이어야 합니다.")
            