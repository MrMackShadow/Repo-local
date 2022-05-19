i = 0
warehouse = []
list_stock = []
print('Вас приветствует программа "Склад"!')
while i != "нет":
    warehouse = dict({'название': input("Введите название товара: "),
                      'цена': input("Введите цену: "),
                      'количество': input('Введите количество: '),
                      'поставщик': input("Введите поставщика: ")})
    list_stock.append(warehouse)
    i = input('Продолжить?(да или нет): ')
print('Товары на складе: ')
print(list_stock)

for ind, el in enumerate(list_stock, 1):
    print(ind, el)

all_names = []
all_prices = []
all_lots = []
all_byers = []

for q in list_stock:
    val = list(q.values())
    all_names.append(val[0])
    all_prices.append(val[1])
    all_lots.append(val[2])
    all_byers.append(val[3])

report = {
    'название': list(set(all_names)),
    'цена': list(set(all_prices)),
    'количество': list(set(all_lots)),
    'поставщик': list(set(all_byers))
}

print(report)
