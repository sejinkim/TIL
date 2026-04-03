import logging
from abc import ABC, abstractmethod
from data_types import PriceTick

class BaseFeed(ABC):
    def __init__(self, symbol:str):
        self.symbol = symbol
        self.logger = logging.getLogger(f"feed.{symbol}")

    @abstractmethod
    def fetch(self) -> PriceTick:
        pass

    def on_error(self, error: Exception):
        self.logger.error(f"{type(error).__name__}. {error}")
