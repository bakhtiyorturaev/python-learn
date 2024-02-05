from threading import *
from time import time, sleep


def one(num):
    sleep(num)


def two(num):
    sleep(num)


x1 = Thread(target=one)
x2 = Thread(target=two)

t1 = time()

x1.start()
x2.start()

t2 = time()
print(t2 - t1)
