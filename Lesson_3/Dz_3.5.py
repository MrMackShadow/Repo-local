def fun_5():

    sum = 0
    x = 0

    while x != "Q" or x != "q":

        x = input('Вводите числа через пробел, что бы посчитать сумму. Если хотите выйти, то введите: "Q": ').split()
        res = 0
        for i in range(len(x)):
            if x[i] == "q" or x[i] == "Q":
                break
            else:
                res = res + int(x[i])
            sum = sum + res
        print(f'Сумма всех введенных чисел ровна: {sum}')

fun_5()