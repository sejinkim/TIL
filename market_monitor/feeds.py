import asyncio
import random
from base_feed import BaseFeed
from data_types import PriceTick
from exceptions import FeedError

class SimulatedFeed(BaseFeed):
    def __init__(self, symbol, base_price: int):
        super().__init__(symbol)
        self.base_price = base_price

    async def fetch(self):
        await asyncio.sleep(1)
        price = int(self.base_price * random.uniform(0.97, 1.03))
        volume = random.randint(100, 5000)

        change = abs(price - self.base_price) / self.base_price
        if change >= 0.02:
            raise FeedError(f"급등락 감지 {self.symbol}")


        return PriceTick(self.symbol, price, volume)
