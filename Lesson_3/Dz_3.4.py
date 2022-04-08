def fun_4(*args):

    x = int(input("Введите любое положительное число: "))
    y = int(input("Введите целое отрицательное число: "))
    i = 0
    res = 1

    while i < abs(y):
        res *= x
        i += 1
    return res
print(fun_4())