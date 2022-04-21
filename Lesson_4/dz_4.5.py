from functools import reduce

def fun_red(a, b):
    return a * b

print(f'Произведение всех чисел {reduce(fun_red, [el for el in range(99, 1001) if el % 2 == 0])}')

