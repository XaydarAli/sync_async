import asyncio
from datetime import datetime

async def async_task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print(" Task 1 completed")

async def async_task2():
    print(" Task 2 started")
    await asyncio.sleep(1)
    print(" Task 2 completed")

async def async_task3():
    print("Task 3 started")
    await asyncio.sleep(3)
    print("Task 3 completed")

async def async_task4():
    print(" Task 4 started")
    await asyncio.sleep(2)
    print(" Task 4 completed")

async def async_task5():
    print(" Task 5 started")
    await asyncio.sleep(1)
    print(" Task 5 completed")

async def async_task6():
    print(" Task 6 started")
    await asyncio.sleep(3)
    print(" Task 6 completed")

async def async_task7():
    print(" Task 7 started")
    await asyncio.sleep(2)
    print(" Task 7 completed")

async def async_task8():
    print(" Task 8 started")
    await asyncio.sleep(1)
    print(" Task 8 completed")


async def async_main():
    await asyncio.gather(
        async_task1(),
        async_task2(),
        async_task3(),
        async_task4(),
        async_task5(),
        async_task6(),
        async_task7(),
        async_task8()
    )
print(datetime.now(), "async_main completed")
asyncio.run(async_main())
