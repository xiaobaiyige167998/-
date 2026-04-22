import asyncio
import time


async def func1():
    print('wwww')
    await asyncio.sleep(2)
    print('wwww')


async def func2():
    print('aaa')
    await asyncio.sleep(5)
    print('aaa')


async def func3():
    print('qqq')
    await asyncio.sleep(1)
    print('qqq')


async def main():
    async with asyncio.TaskGroup() as f:
        f.create_task(func1())
        f.create_task(func2())
        f.create_task(func3())


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2-t1)







