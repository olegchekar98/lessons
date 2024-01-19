from multiprocessing import Pool, cpu_count


def worker(val):
    return val ** 2


if __name__ == '__main__':

    with Pool(2) as pool:
        r = pool.map(worker, range(10))
        print(r)

        iterator = pool.imap(worker, range(10))
        print(iterator)
        [print(el, end=" ") for el in iterator]
