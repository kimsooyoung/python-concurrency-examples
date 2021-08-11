# Code from tutorialedge.net
# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/
#
# Mutex Lock

import asyncio

lock = asyncio.Lock()
counter = 0


async def myCoroutine():
    global lock, counter

    async with lock:
        while True:
            counter += 1
            await asyncio.sleep(1)
            print(f"I am myCoroutine, And Current Counter is {counter} ")


async def mySecondCoroutine():
    global lock, counter

    async with lock:
        while True:
            counter += 1
            await asyncio.sleep(1)
            print(f"I am mySecondCoroutine, And Current Counter is {counter} ")


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(myCoroutine())
    asyncio.ensure_future(mySecondCoroutine())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
