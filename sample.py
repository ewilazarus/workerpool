from wpool import IOWorkerPool
import time
import random

def consumer(i):
    time.sleep(random.random())
    print(i)

if __name__ == '__main__':
    with IOWorkerPool() as pool:
        while True:
            for i in range(100):
                pool.submit(consumer, i)
            time.sleep(15)
