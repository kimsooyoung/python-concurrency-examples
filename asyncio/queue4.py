import asyncio
import random

counter = 0


async def produce(queue):
    global counter

    while True:
        # produce an item
        print("producing {}".format(counter))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        item = str(counter)
        # put the item in the queue
        await queue.put(item)
        counter += 1

    # indicate the producer is done
    await queue.put(None)


async def consume(queue):
    while True:
        # wait for an item from the producer
        item = await queue.get()
        if item is None:
            # the producer emits None to indicate that it is done
            break

        # process the item
        print("consuming item {}...".format(item))
        # simulate i/o operation using sleep
        # await asyncio.sleep(random.random())


loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop)
producer_coro = produce(queue)
consumer_coro = consume(queue)
loop.run_until_complete(asyncio.gather(producer_coro, consumer_coro))
loop.close()
