from concurrent.futures import ThreadPoolExecutor
def func1(i):
    print(i)



if __name__ == '__main__':
    with ThreadPoolExecutor(10) as tp:
        for i in range(100):
            tp.submit(func1,i)