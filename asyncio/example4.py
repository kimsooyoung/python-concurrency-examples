# Code from tutorialedge.net
# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

import asyncio


async def myCoroutine():
    while True:
        await asyncio.sleep(1)
        print("This is my coroutine")


async def mySecondCoroutine():
    while True:
        await asyncio.sleep(1)
        print("This is my Second coroutine")


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

# Result
#
# $ python3 asyncio/example4.py
# This is my coroutine
# This is my Second coroutine
# This is my coroutine
# This is my Second coroutine
# This is my coroutine
# This is my Second coroutine
# This is my coroutine
# This is my Second coroutine
# ...
