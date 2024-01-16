# example of a deadlock caused by a thread waiting on itself
from threading import Thread
from threading import Lock
from threading import RLock


# task to be executed in a new thread
def task(lock):
    print('Thread acquiring lock...')
    with lock:
        print('Thread acquiring lock again...')
        with lock:
            print('Thread')
            # will never get here
            pass


# create the mutex lock
#lock = Lock()
lock = RLock()
# create and configure the new thread
thread = Thread(target=task, args=(lock,))
# start the new thread
thread.start()
# wait for threads to exit...
thread.join()