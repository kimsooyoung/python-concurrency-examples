# Code from tutorialedge.net
# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/
#
# Resource sharing btw event loops

import asyncio

counter = 0


def printGreeting(greeting):
    print(greeting)


async def myCoroutine():
    global counter

    while True:
        counter += 1
        await loop.run_in_executor(
            None, printGreeting, f"This is my coroutine {counter}"
        )


async def mySecondCoroutine():
    global counter

    while True:
        counter += 1
        await loop.run_in_executor(
            None, printGreeting, f"This is my Second coroutine {counter} "
        )


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
