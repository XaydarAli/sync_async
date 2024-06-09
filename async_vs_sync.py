import asyncio
import time
from datetime import datetime

def sync_task1():
    print(datetime.now(), "sync_task1 started")
    time.sleep(2)
    print(datetime.now(), "sync_task1 completed")

def sync_task2():
    print(datetime.now(), "sync_task2 started")
    time.sleep(1)
    print(datetime.now(), "sync_task2 completed")

async def async_task1():
    print(datetime.now(), "async_task1 started")
    await asyncio.sleep(2)
    print(datetime.now(), "async_task1 completed")

async def async_task2():
    print(datetime.now(), "async_task2 started")
    await asyncio.sleep(1)
    print(datetime.now(), "async_task2 completed")

def sync_main():
    print(datetime.now(), " sync_main started")
    sync_task1()
    sync_task2()
    print(datetime.now(), "sync_main completed")

async def async_main():
    print(datetime.now(), "async_main started")
    await asyncio.gather(
        async_task1(),
        async_task2()
    )
    print(datetime.now(), "async_main completed")

async def run_async_main():
    await async_main()

sync_main()

asyncio.run(run_async_main())
