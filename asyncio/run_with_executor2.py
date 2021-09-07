# threading required for two websocket clients
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
    loop_1 = asyncio.new_event_loop()
    asyncio.set_event_loop(loop_1)

    asyncio.ensure_future(HelloWithName("First Man"))
    asyncio.ensure_future(HelloWithName("Second Man"))

    loop_1.run_forever()


def secondFunc():
    loop_2 = asyncio.new_event_loop()
    asyncio.set_event_loop(loop_2)

    asyncio.ensure_future(HelloWithName("Third Man"))
    asyncio.ensure_future(HelloWithName("Fourth Man"))

    loop_2.run_forever()


# Example 1 Concurrency with Futures (More modern method)
futures_list = []

# worker = min(10, len(WORK_LIST))
with ThreadPoolExecutor() as excutor:
    # Register two infinite loops
    future = excutor.submit(firstFunc)
    futures_list.append(future)
    print("Scheduled future {}".format(future))

    future2 = excutor.submit(secondFunc)
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
