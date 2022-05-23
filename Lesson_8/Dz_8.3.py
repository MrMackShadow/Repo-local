class NotNumber(ValueError):
    pass


my_list = []
while True:
    try:
        num = input('Вводите числа,если вы хотите завершить, то нажмите "Q": ')
        if num == 'Q':
            break
        if not num.isdigit():
            raise NotNumber(num)
        my_list.append(int(num))
    except NotNumber as ex:
        print('Нужно ввести только число!', ex)
print(my_list)
