import asyncio


async def producer(queue, item):
    await queue.put(item)


async def consumer(queue):
    val = await queue.get()
    print("val = %d" % val)


async def main():
    queue = asyncio.Queue()
    while True:
        await asyncio.gather(consumer(queue), producer(queue, 1))
        await consumer(queue)
        await producer(queue, 1)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
