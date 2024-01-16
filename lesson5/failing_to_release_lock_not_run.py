# example of a deadlock caused by a thread failing to release a lock
from time import sleep
from threading import Thread
from threading import Lock


# task to be executed in a new thread
def task(lock):
    # acquire the lock
    print('Thread acquiring lock...')
    with lock:
        lock.acquire()
        # fail
        raise Exception('Something bad happened')
        # release the lock (never gets here)
        print('Thread releasing lock...')
        lock.release()


# create the mutex lock
lock = Lock()
# create and configure the new thread
thread = Thread(target=task, args=(lock,))
# start the new thread
thread.start()
# wait a while
sleep(1)
# acquire the lock
print('Main acquiring lock...')

# do something...
# release lock (never gets here)
lock.release()