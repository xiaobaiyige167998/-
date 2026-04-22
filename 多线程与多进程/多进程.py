from multiprocessing import Process
import time
def func():
    for i in range(1000):
        print('子进程',i)

if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    for i in range(1000):
        print('你爹',i)
        time.sleep(0.01)   #主动让出cpu让显示更明显
