'''
Assignment 1: Race Conditions, Lock, Semaphore
'''

# Race Conditions
import asyncio
import time
counter=0

async def increment():
    global counter
    print("increment reads", counter)
    await asyncio.sleep(2)

    temp = counter
    await asyncio.sleep(0)   

    temp += 1
    counter = temp
    print("increment writes", counter)


async def decrement():
    global counter
    print("decrement reads", counter)
    await asyncio.sleep(2)

    temp = counter
    await asyncio.sleep(0)

    temp -= 1
    counter = temp
    print("decrement writes", counter)



async def counterTask():
    p1=asyncio.create_task(increment())
    p2=asyncio.create_task(decrement())
    await p1  
    await p2    

# asyncio.run(counterTask())


# Lock

counter2=0
lock = asyncio.Lock()

async def increment_lock():
    global counter2

    async with lock:
        print("Increament --> Lock")
        current=counter2
        await asyncio.sleep(2)
        counter2=current+1
        print("increment counter", counter2)

async def decrement_lock():
    global counter2

    async with lock:
        print("Decrement --> lock")
        current = counter2
        await asyncio.sleep(2)
        counter2 = current - 1
        print("Decrement:", counter2) 


async def main():
    timer1=time.time()
    task1=asyncio.create_task(increment_lock())
    task2=asyncio.create_task(decrement_lock())

    await task1
    await task2
    print("Final counter:", counter2)
    timer2=time.time()
    print(timer2-timer1)


# asyncio.run(main())





# semaphore
semaphore = asyncio.Semaphore(3)


async def worker(number):
    async with semaphore:
        print(f"Task {number} started")
        await asyncio.sleep(2)
        print(f"Task {number} finished")


async def main():
    tasks = [
        asyncio.create_task(worker(i))
        for i in range(1, 11)
    ]

    await asyncio.gather(*tasks)


asyncio.run(main())
