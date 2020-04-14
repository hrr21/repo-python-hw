from itertools import count
from math import factorial


def generator():
    for el in count(1):
        yield factorial(el)


fibo_gen = generator()
n = 0
for el in fibo_gen:
    if n < 15:
        print(el)
        n += 1
    else:
        break
