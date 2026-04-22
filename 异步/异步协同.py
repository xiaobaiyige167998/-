import asyncio
import time

async def func1():   #将函数定义为异步函数
    print('wwww')
    await asyncio.sleep(2)   #将sleep挂起
    print('wwww')


async def func2():  #将函数定义为异步函数
    print('aaaa')
    await asyncio.sleep(3)   #将sleep挂起
    print('aaaa')


async def func3():  #将函数定义为异步函数
    print('qqqq')
    await asyncio.sleep(4)   #将sleep挂起
    print('qqqq')


async def main():  #将函数定义为异步函数

    async with asyncio.TaskGroup() as f:   #创建需要进行异步的任务
        f.create_task(func3())      #调用函数，生成协程对象，通过TaskGroup包装成一个Task（异步任务）
        f.create_task(func1())      #调用函数，生成协程对象，通过TaskGroup包装成一个Task（异步任务）
        f.create_task(func2())      #调用函数，生成协程对象，通过TaskGroup包装成一个Task（异步任务）


if __name__ == '__main__':
    t1=time.time()
    asyncio.run(main())   #创建一个全新的事件循环，运行异步任务
    t2=time.time()
    print(t2-t1)   #查看执行所需的时间