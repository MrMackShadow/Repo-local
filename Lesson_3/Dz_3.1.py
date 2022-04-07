def fun_1():
    try:
        number_1 = int(input("Введите первое число: "))
        number_2 = int(input("Введите второе число: "))
        result = number_1 / number_2
        return result
    except ZeroDivisionError:
        return "На ноль делить нельзя"

print(fun_1())