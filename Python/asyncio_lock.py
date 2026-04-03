'''
asyncio.lock을 사용하여 두 출금 코루틴이 동시에 실행되지 않도록 하는 예제
'''
# 어떤 일이 생기는지 살펴봅시다.
# import asyncio

# balance = 100000  # 잔고

# async def withdraw(name, amount):
#     global balance
#     print(f"{name}: 잔고 확인 → {balance}원")
#     await asyncio.sleep(0)   # 다른 코루틴에게 잠깐 양보
#     balance -= amount
#     print(f"{name}: 출금 완료 → 잔고 {balance}원")

# async def main():
#     await asyncio.gather(
#         withdraw("출금A", 70000),
#         withdraw("출금B", 70000),
#     )
#     print(f"최종 잔고: {balance}원")

# asyncio.run(main())

# asyncio.lock을 사용하게 되면?
import asyncio

balance = 100000
lock = asyncio.Lock()   # 자물쇠

async def withdraw(name, amount):
    global balance
    async with lock:    # 자물쇠 잠금 — 한 번에 하나만 진입 가능
        print(f"{name}: 잔고 확인 → {balance}원")
        await asyncio.sleep(0)
        if balance < amount:
            print(f"{name}: 잔고 부족!")
            return
        balance -= amount
        print(f"{name}: 출금 완료 → 잔고 {balance}원")

async def main():
    await asyncio.gather(
        withdraw("출금A", 70000),
        withdraw("출금B", 70000),
    )
    print(f"최종 잔고: {balance}원")

asyncio.run(main())