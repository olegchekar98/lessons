from multiprocessing import Process, Queue, cpu_count
from time import sleep
import sys


def worker(qu: Queue, name):
    print(f"{name} started!")
    val = qu.get()
    print(f"{name} {val ** 2}")
    sys.exit(0)  # Если не ноль, то это код ошибки


if __name__ == "__main__":
    qu = Queue()

    # if cpu_count() < 12:
    #     raise ValueError
    cores_count = cpu_count()
    print(cores_count)

    for elem in range(cores_count):
        pr1 = Process(target=worker, args=(qu, elem))
        pr1.start()

    qu.put(10)
    sleep(5)
    qu.put(5)
    qu.put(15)
    qu.put(5)
    qu.put(15)
    qu.put(15)
    qu.put(5)
    qu.put(15)
    qu.put(5)
    qu.put(15)
    qu.put(50)
    qu.put(150)
