def fun_list():

    first_list = [12, 34, 54, 13, 45]
    second_list = [el for i, el in enumerate(first_list) if first_list[i - 1] < first_list[i]]
    print(f'Old list {first_list}')
    print(f'Your new list {second_list}')

fun_list()