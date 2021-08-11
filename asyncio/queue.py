# Code from ksindi
# https://gist.github.com/ksindi/3526b5d0942f23b1d6ded149fe395821
#
# AsyncIO Queue, register and cancelling Usage

import asyncio
import random
import time


async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f"{name} has slept for {sleep_for:.2f} seconds")


async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f"worker-{i}", queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print("====")
    print(f"3 workers slept in parallel for {total_slept_for:.2f} seconds")
    print(f"total expected sleep time: {total_sleep_time:.2f} seconds")


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

#### Result ####
#
# worker-2 has slept for 0.30 seconds
# worker-1 has slept for 0.45 seconds
# worker-0 has slept for 0.81 seconds
# worker-2 has slept for 0.67 seconds
# worker-0 has slept for 0.23 seconds
# worker-0 has slept for 0.33 seconds
# worker-1 has slept for 0.96 seconds
# worker-2 has slept for 0.71 seconds
# worker-2 has slept for 0.08 seconds
# worker-0 has slept for 0.64 seconds
# worker-2 has slept for 0.29 seconds
# worker-1 has slept for 0.76 seconds
# worker-0 has slept for 0.80 seconds
# worker-1 has slept for 0.67 seconds
# worker-2 has slept for 0.99 seconds
# worker-0 has slept for 0.84 seconds
# worker-2 has slept for 0.67 seconds
# worker-1 has slept for 0.90 seconds
# worker-0 has slept for 0.33 seconds
# worker-2 has slept for 0.35 seconds
# ====
# 3 workers slept in parallel for 4.07 seconds
# total expected sleep time: 11.79 seconds
