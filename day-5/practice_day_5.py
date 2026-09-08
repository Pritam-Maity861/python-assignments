import asyncio
import time

async def task(name):
    print(f"Task {name} Started!!")
    await asyncio.sleep(2)
    print(f"Task {name} finished!!")
    return name


async def run_my_func():
    timer1=time.time()
    task1=await task("A")
    task2=await task("B")
    task3=await task("C")
    timer2=time.time()
    print(timer2-timer1)

# result= asyncio.run(run_my_func())

async def run_my_func_async():
    timer1=time.time()
    task1=asyncio.create_task(task("A"))
    task2=asyncio.create_task(task("B"))
    task3=asyncio.create_task(task("C"))
    await task1
    await task2
    await task3
    timer2=time.time()
    print(timer2-timer1)

# asyncio.run(run_my_func_async())

async def run_my_func_gather():
    result=await asyncio.gather(task(1),task(2),task(3))
    print(result)

asyncio.run(run_my_func_gather())
        
