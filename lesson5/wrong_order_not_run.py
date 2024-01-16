# example of a deadlock caused by acquiring locks in a different order
from time import sleep
from threading import Thread
from threading import Lock


# task to be executed in a new thread
def task(number, lock1, lock2):
    # acquire the first lock
    print(f'Thread {number} acquiring lock 1...')
    with lock1:
        # wait a moment
        sleep(1)
        # acquire the next lock
        print(f'Thread {number} acquiring lock 2...')
        with lock2:
            print(f'Thread {number} acquiring lock')
            # never gets here..
            pass


# create the mutex locks
lock1 = Lock()
lock2 = Lock()
# create and configure the new threads
thread1 = Thread(target=task, args=(1, lock1, lock2))
thread2 = Thread(target=task, args=(2, lock1, lock2))
# start the new threads
thread1.start()
thread2.start()
# wait for threads to exit...
thread1.join()
thread2.join()
