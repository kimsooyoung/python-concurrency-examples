import asyncio

# An asyncio Queue has put_nowait and get coroutine
q = asyncio.Queue()


def put_logic():
    q.put_nowait("Hi!")


# Sends data each second
async def sender():
    while True:
        # await asyncio.sleep(1)
        # q.put_nowait("hi!")
        # asyncio.ensure_future(q.put("data"))
        await q.put("hi!")
        # await loop.run_in_executor(None, put_logic)


# Receives the data
async def receiver():
    while True:
        # await q.join()
        data = await q.get()
        print("Received:", data)


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(sender())
    asyncio.ensure_future(receiver())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    # loop.close()
