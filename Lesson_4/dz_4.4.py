def fun_double():

    a_list = [2, 4, 5, 6, 7, 2, 23, 4, 66, 6, 7, 12, 23, 65]
    b_list = [el for el in a_list if a_list.count(el) == 1]
    c_list = [el for el in a_list if a_list.count(el) >= 2]
    print(f' Не повторяются числа: {b_list}')
    print(f' Повторяются числа: {c_list}')

fun_double()

