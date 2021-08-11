# Code from tutorialedge.net
# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

import asyncio


async def myCoroutine():
    print("This is my coroutine")


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(myCoroutine())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()

# Result
#
# $ python3 asyncio/example2.py
# This is my coroutine
# (Cannot reach to finally)
