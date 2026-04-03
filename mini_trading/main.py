from orders.order_types import OrderType, Order
from orders.exceptions import KISError, AuthError, OrderError

# print("__name__의 값:", __name__)

# order = Order("005930", 10, 71000, OrderType.LIMIT)
# print(order)

# def submit_order(symbol, quantity):
#     if quantity <= 0:
#         raise OrderError("수량은 0보다 커야 합니다", symbol=symbol)

# try:
#     submit_order("005930", -1)
# except OrderError as e:
#     print(f"주문 오류: {e}")
#     print(f"문제 종목: {e.symbol}")
# except KISError as e:
#     print(f"KIS 오류: {e}")

# try:
#     raise OrderError("잘못된 수량", symbol="005930")
# except KISError as e:
#     print(f"잡혔어요: {e}")
    

'''

`main.py`를 터미널에서 실행해보기:
'''
# # 2. 로깅
# import logging
# from logging.handlers import RotatingFileHandler

# # 파일로 저장하는 핸들러
# file_handler = RotatingFileHandler(
#     "trading.log",        # 저장할 파일 이름
#     maxBytes=1024*1024,   # 1MB 넘으면 새 파일로
#     backupCount=5         # 최대 5개 파일 보관
# )

# # 터미널 출력 핸들러
# stream_handler = logging.StreamHandler()

# # 로거 설정
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s %(levelname)s %(name)s - %(message)s",
#     handlers=[file_handler, stream_handler]  # 둘 다 동시에
# )

# logger = logging.getLogger("trading.main")

# # print 대신 이렇게
# logger.debug("디버그: 상세 실행 정보")
# logger.info("정보: 서버 시작됨")
# logger.warning("경고: 잔고 부족")
# logger.error("오류: 주문 실패")

# 3. async
import time

# def fetch_price():
#     print("가격 조회 시작...")
#     time.sleep(2)   # KIS API 응답 대기 (2초)
#     print("가격 조회 완료")

# def fetch_balance():
#     print("잔고 조회 시작...")
#     time.sleep(2)   # KIS API 응답 대기 (2초)
#     print("잔고 조회 완료")

# start = time.time()
# fetch_price()
# fetch_balance()
# print(f"총 소요시간: {time.time() - start:.1f}초")

'''
4초! 두 작업이 순서대로 실행됐으니까 2 + 2 = 4초예요.
그런데 생각해보면 — fetch_price()가 API 응답을 기다리는 2초 동안 CPU는 아무것도 안 하고 있어요. 그 시간에 fetch_balance()를 시작하면 2초로 끝날 수 있는데요.
이게 바로 async가 해결하는 문제예요. 이제 같은 코드를 async로 바꿔봐요:
'''

# import asyncio

# async def fetch_price():    # 이 함수 안에서 await를 쓸 수 있다라는 선언
#     print("가격 조회 시작...")
#     await asyncio.sleep(2)  # "여기서 잠깐 기다려야 해. 그 동안 다른 거 해도 돼" 라는 신호
#     print("가격 조회 완료")

# async def fetch_balance():
#     print("잔고 조회 시작...")
#     await asyncio.sleep(2)
#     print("잔고 조회 완료")

# async def main():
#     start = time.time()
    
#     # await asyncio.gather(
#     #     fetch_price(),
#     #     fetch_balance()
#     # )

#     # 위의 gather 대신 create_task. trading_server에서 더 자주 쓰이는 패턴.
#     task1 = asyncio.create_task(fetch_price())
#     task2 = asyncio.create_task(fetch_balance())
#     await task1
#     await task2

#     print(f"총 소요시간: {time.time() - start:.1f}초")

# asyncio.run(main()) # 비동기 세계로 진입하는 문. 이벤트 루프를 만들고 실행.

# 4. gather()와 create_task() 차이점 알아보기
# 4-1. gather()
# import asyncio

# async def fetch_price(symbol):
#     print(f"{symbol} 조회 시작...")
#     await asyncio.sleep(1)
#     return f"{symbol}: 71000원"   # 결과값을 돌려줌

# async def main():
#     # 세 종목 동시 조회, 결과를 한 번에 받음
#     results = await asyncio.gather(
#         fetch_price("005930"),
#         fetch_price("000660"),
#         fetch_price("005380"),
#     )
#     print("조회 완료:", results)

# asyncio.run(main())

# 4-2. create_task()
import asyncio

async def heartbeat():
    # 서버가 살아있는 동안 계속 돌아가는 작업
    while True:
        print("♥ 서버 살아있음")
        await asyncio.sleep(1)

async def main():
    # 백그라운드에서 시작만 해놓고
    task = asyncio.create_task(heartbeat())

    # 나는 다른 일을 함
    print("전략 로딩 중...")
    await asyncio.sleep(2)
    print("종목 마스터 로딩 중...")
    await asyncio.sleep(2)

    # 다 끝나면 백그라운드 태스크 취소
    task.cancel()
    print("서버 종료")

asyncio.run(main())