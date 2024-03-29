import sys
from multiprocessing import Process, Semaphore, current_process, Manager
from random import randint
from time import sleep


def worker(semaphore: Semaphore, r: dict):
    print('Wait')
    with semaphore:
        name = current_process().name
        print(f'Work {name}')
        delay = randint(1, 2)
        r[name] = delay
        sleep(4)  # Імітуємо якусь роботу
        sys.exit(0)


if __name__ == '__main__':
    semaphore = Semaphore(3)
    with Manager() as m:
        result = m.dict()
        prs = []
        for num in range(10):
            pr = Process(name=f'Process-{num}', target=worker, args=(semaphore, result))
            pr.start()
            prs.append(pr)

        [pr.join() for pr in prs]

        print(result)

    print('End program')