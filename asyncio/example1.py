# Code from tutorialedge.net
# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

import asyncio


async def myCoroutine():
    print("This is my coroutine")


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(myCoroutine())
finally:
    loop.close()

# Result
#
# $ python3 asyncio/example1.py
# This is my coroutine
