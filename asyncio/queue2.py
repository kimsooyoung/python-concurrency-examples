# Code from hulk89
# https://hulk89.github.io/python/2018/08/07/asyncio_queue/

import asyncio
import sys
from functools import partial


def handle_stdin(queue):
    data = sys.stdin.readline().strip()
    if data == "q":
        loop = asyncio.get_event_loop()
        loop.remove_reader(sys.stdin)
    queue.put_nowait(data)
    # asyncio.ensure_future(queue.put(data))


async def tick(queue):
    stop = False
    while not stop:

        data = await queue.get()
        print("Data received: {}".format(data))
        if data == "q":
            stop = True
    print("tick finished.")


def main():
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()
    loop.add_reader(sys.stdin, partial(handle_stdin, queue))
    loop.run_until_complete(tick(queue))
    loop.close()


if __name__ == "__main__":
    main()

#### Result ####
#
# Data received: THis
# is
# Data received: is
# test
# Data received: test
