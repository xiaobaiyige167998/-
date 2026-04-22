

# 导入模块
from threading import Thread   #线程类

# # (1)第一种写法
# def func():
#     for i in range(1000):
#         print('func',i)
#
#
# if __name__ == '__main__':
#     t = Thread(target=func)   #创建了一个线程对象t，如果执行的话，会执行func()函数
#     t.start()
#     for i in range(1000):
#         print('main',i)
#


# (2)第二种写法


class MyThread(Thread):   #  MyThread继承了父类Thread，就会有Thread的特性
    def run(self):   #  run是固定的    -----> 当线程被执行的时候，被执行的就是run()
        for i in range(1000):
            print('次线程',i)


if __name__ == '__main__':
    t = MyThread()
    t.start()   #开启线程   不能用 t.run()

    for i in range(1000):
        print('主线程',i)