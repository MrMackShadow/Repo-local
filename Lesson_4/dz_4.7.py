from math import factorial
from itertools import count

def fact():
    for el in count(1):
        yield factorial(el)

x = 0
n = int(input("Введите число, до которого нужно посчитать: "))
for i in fact():
    if x < n:
        print(i)
        x += 1
    else:
        break
fact()