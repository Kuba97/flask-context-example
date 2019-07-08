import logging
from functools import partial
from multiprocessing import Pool

import requests

logging.getLogger().setLevel(logging.WARNING)


def main():
    for _ in range(0, 10):
        multiprocessing_inc_dec()
        # request_set(number=0)


def simple_increment_decrement():
    request_get()

    request_increment()
    request_get()

    request_decrement()
    request_get()


def multiprocessing_inc_dec():
    request_get()

    n_iter_inc = 1000
    n_iter_dec = 1000
    funcs = [partial(increment_loop, n_iter=n_iter_inc),
             partial(decrement_loop, n_iter=n_iter_dec),
             partial(decrement_loop, n_iter=n_iter_dec)]
    with Pool(processes=3) as pool:
        pool.map(exec_func, funcs)

    request_get()
    print('\n')


def request_increment():
    logging.info('Incrementing...')
    requests.post('http://127.0.0.1:5000/increment')


def request_decrement():
    logging.info('Decrementing...')
    requests.post('http://127.0.0.1:5000/decrement')


def request_get():
    print(requests.get('http://127.0.0.1:5000/access').json())


def request_set(number=0):
    requests.post('http://127.0.0.1:5000/set', json={'number': number})


def exec_func(func):
    func()


def increment_loop(n_iter=256):
    for i in range(0, n_iter):
        request_increment()


def decrement_loop(n_iter=256):
    for i in range(0, n_iter):
        request_decrement()


if __name__ == '__main__':
    request_set()
    main()
