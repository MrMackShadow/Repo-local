from itertools import count
from itertools import cycle


def one_func():
    for el in count(int(input('Please inter number from 1 to 10: '))):
        if el > 30:
            break
        else:
            print(el)

    c = 0
    list = ["red", "green", "black", "white"]
    for i in cycle(list):
        if c > 10:
            break
        else:
            print(i)
        c += 1


one_func()

