# referenced from : https://velog.io/@rorhcdream/python-asyncio-with-threads

import threading
import asyncio
import time


# Normal Inifiniy Loop
def firstUpdater():
    while True:
        print("Hello I am firstUpdater")
        time.sleep(0.5)


def secondUpdater():
    while True:
        print("Hello I am secondUpdater")
        time.sleep(1)


# Inifiniy Loop with asyncio
def asyncSecondUpdater():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def update_async():
        while True:
            print("Hello I am secondUpdater")
            await asyncio.sleep(1)

    loop.run_until_complete(update_async())


t1 = threading.Thread(target=firstUpdater, daemon=True)

# uncomment below lines and check difference btw two methods
# t2 = threading.Thread(target=secondUpdater, daemon=True)
t2 = threading.Thread(target=asyncSecondUpdater, daemon=True)
t1.start()
t2.start()

# join이 없으면 한번 실행하고 끝나버린다.
t1.join()
t2.join()
