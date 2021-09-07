# Class Version of run_with_executor2.py
import asyncio

# futures required for two websocket clients
from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    wait,
    as_completed,
)


async def HelloWithName(name="Pythonic"):
    while True:
        print(f"Hello, {name}")
        await asyncio.sleep(2)


# get_event_loop -> RuntimeError: There is no current event loop in thread 'ThreadPoolExecutor-0_0'.
# only new_event_loop works
def firstFunc():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    asyncio.ensure_future(HelloWithName("First Man"))
    asyncio.ensure_future(HelloWithName("Second Man"))

    loop.run_forever()


def secondFunc():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    asyncio.ensure_future(HelloWithName("Third Man"))
    asyncio.ensure_future(HelloWithName("Fourth Man"))

    loop.run_forever()


class FirstClass(object):
    def __init__(self):
        super().__init__()

    async def HelloWithName(self, name="Pythonic"):
        while True:
            print(f"Hello, {name}")
            await asyncio.sleep(2)

    def run(self):
        # 이거 꼭 여기 적어줘야 한다!!
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)

        asyncio.ensure_future(self.HelloWithName("First Man"))
        asyncio.ensure_future(self.HelloWithName("Second Man"))

        self._loop.run_forever()

    def executor_run(self, executor):
        future = excutor.submit(self.run)
        return future


class SecondClass(object):
    def __init__(self):
        super().__init__()

    async def HelloWithName(self, name="Pythonic"):
        while True:
            print(f"Hello, {name}")
            await asyncio.sleep(2)

    def run(self):
        try:
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)

            asyncio.ensure_future(HelloWithName("Third Man"))
            asyncio.ensure_future(HelloWithName("Fourth Man"))

            self._loop.run_forever()
        except Exception as e:
            print(e)


# 2번 예제의 함수형은 잘되는데, 클래스로 오기만 하면 ㅄ이 된다.
# RuntimeWarning: coroutine 'FirstClass.HelloWithName' was never awaited
# Example 1 Concurrency with Futures (More modern method)
if __name__ == "__main__":

    futures_list = []

    second_class = SecondClass()

    # worker = min(10, len(WORK_LIST))
    with ThreadPoolExecutor() as excutor:
        # Register two infinite loops
        first_class = FirstClass()
        future = excutor.submit(first_class.run)
        futures_list.append(future)
        print("Scheduled future {}".format(future))

        future2 = excutor.submit(second_class.run)
        futures_list.append(future2)
        print("Scheduled future {}".format(future2))

    for future in as_completed(futures_list):
        result = future.result()
        done = future.done()
        cancelled = future.cancelled

        # future 결과 확인
        # print("Future Result : {}, Done : {}".format(result, done))
        # print("Future Cancelled : {}".format(cancelled))

# Result
#
# Hello, Second Man
# Hello, Third Man
# Hello, First Man
# Hello, Fourth Man
# Hello, Second Man
# Hello, Third Man
# Hello, Fourth Man
# Hello, First Man
# Hello, Second Man
# Hello, First Man
# Hello, Third Man
# Hello, Second Man
# Hello, Fourth Man
