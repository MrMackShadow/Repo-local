def fun_3(*args):
    num_1 = int(input("Введите первое число: "))
    num_2 = int(input("Введите второе число: "))
    num_3 = int(input("Введите третье число: "))

    if num_1 >= num_2 and num_3 >= num_2:
        return num_1 + num_3
    elif num_1 >= num_3 and num_2 >= num_3:
        return num_1 + num_2
    elif num_2 >= num_1 and num_3 >= num_1:
        return num_2 + num_3
print("Результат: ", fun_3())