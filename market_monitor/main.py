'''
아래 기능을 구현해요:

**`monitor(feed)` 비동기 함수:**
- 5번 반복해서 `feed.fetch()`를 호출
- 결과를 로거로 출력: `"005930 | 71200원 | 거래량: 1500"`
- `FeedError` 발생 시 `feed.on_error()`로 처리하고 계속 진행

**`main()` 비동기 함수:**
- 3개 종목 `SimulatedFeed` 생성
    - `"005930"` (삼성전자) 기준가 `71000`
    - `"000660"` (SK하이닉스) 기준가 `180000`
    - `"005380"` (현대차) 기준가 `245000`
- 3개를 **동시에** 모니터링 (`create_task` + `gather`)

**`if __name__ == "__main__"`** 으로 실행

---

### 목표 출력 (예시)
```
2026-04-02 17:00:01 INFO feed.005930 — 005930 | 71200원 | 거래량: 1823
2026-04-02 17:00:01 INFO feed.000660 — 000660 | 181500원 | 거래량: 4201
2026-04-02 17:00:01 INFO feed.005380 — 005380 | 243000원 | 거래량: 992
2026-04-02 17:00:02 INFO feed.005930 — 005930 | 70100원 | 거래량: 2100
2026-04-02 17:00:02 ERROR feed.005930 — FeedError: 급등락 감지 005930
...

'''
import logging
import asyncio

from exceptions import FeedError
from feeds import SimulatedFeed

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s"
)

async def monitor(feed):
    logger = logging.getLogger(f"feed.{feed.symbol}")
    for _ in range(5):
        try:
            tick = await feed.fetch()
            logger.info(f"{tick.symbol} | {tick.price:,}원 | 거래량: {tick.volume:,}")
        except FeedError as e:
            feed.on_error(e)

async def main():
    feeds = [
        SimulatedFeed("005930", 71000),
        SimulatedFeed("000660", 180000),
        SimulatedFeed("005380", 245000),
    ]

    tasks = [asyncio.create_task(monitor(feed)) for feed in feeds]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
        asyncio.run(main())