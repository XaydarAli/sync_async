import time
from datetime import datetime

def sync_task1():
    print(" Task 1 started")
    time.sleep(2)
    print(" Task 1 completed")

def sync_task2():
    print(" Task 2 started")
    time.sleep(1)
    print(" Task 2 completed")

def sync_task3():
    print(" Task 3 started")
    time.sleep(3)
    print(" Task 3 completed")

def sync_task4():
    print(" Task 4 started")
    time.sleep(2)
    print(" Task 4 completed")

def sync_task5():
    print(" Task 5 started")
    time.sleep(1)
    print(" Task 5 completed")

def sync_task6():
    print(" Task 6 started")
    time.sleep(3)
    print(" Task 6 completed")

def sync_task7():
    print(" Task 7 started")
    time.sleep(2)
    print("Task 7 completed")

def sync_task8():
    print(" Task 8 started")
    time.sleep(1)
    print(" Task 8 completed")

def sync_main():
    sync_task1()
    sync_task2()
    sync_task3()
    sync_task4()
    sync_task5()
    sync_task6()
    sync_task7()
    sync_task8()
print(datetime.now(), "Sync_main completed")
sync_main()
