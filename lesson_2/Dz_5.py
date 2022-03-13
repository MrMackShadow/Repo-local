list = [8, 5, 7, 2, 3]
print('Это список рейтинга: ', list)
us_an = int(input('Введите натуральное целое число которое будет обозначать новый рейтинг: '))
list.append(us_an)
list.sort()
list.reverse()
print('Рейтинг обновился: ', list)



