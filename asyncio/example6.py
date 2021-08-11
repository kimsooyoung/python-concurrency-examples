# Code from tutorialedge.net
# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

import asyncio


def printGreeting(greeting):
    print(greeting)


async def myCoroutine():
    while True:
        await loop.run_in_executor(None, printGreeting, "This is my coroutine")


async def mySecondCoroutine():
    while True:
        await loop.run_in_executor(None, printGreeting, "This is my Second coroutine")


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
