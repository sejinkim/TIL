from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Optional

# 조건 1 - OrderType Enum 만들기
'''
아래 세 가지 주문 타입을 가진 OrderType을 만들어요:

- LIMIT = "00" (지정가)
- MARKET = "01" (시장가)
- CANCEL = "02" (취소)
'''
class OrderType(str, Enum):
    LIMIT   = "00"      # 지정가
    MARKET  = "01"      # 시장가
    CANCEL  = "02"      # 취소

# 조건 2 - Order dataclass 만들기
'''
아래 속성을 가진 Order를 만들어요:
- symbol: str — 종목코드
- quantity: int — 수량
- price: int — 가격
- order_type: OrderType — 주문 타입 (기본값: OrderType.LIMIT)

그리고 __post_init__에서 아래를 검증해요:
- quantity가 0 이하면 ValueError 발생
- price가 0 미만이면 ValueError 발생
'''

@dataclass  #인자 이름과 속성 이름을 반복하여 쓸 필요가 없게 해 줌.
class Order:
    symbol: str
    quantity: int
    price: Optional[int] = None
    order_type: OrderType = OrderType.LIMIT

    def __post_init__(self):    # __init__ 실행 직후 자동으로 호출됨. 주로 데이터 검증에 씀.
        if self.quantity <= 0:
            raise ValueError("quantity must be > 0")

        if self.price is not None and self.price < 0:
            raise ValueError("price must be >= 0")

# print("order_types의 __name__:", __name__)

# if __name__ == "__main__":
#     order = Order("005930", 10, 71000, OrderType.LIMIT)
#     print("테스트 주문:", order)