class Sklad:
    def __init__(self):
        self.dict = {}
        self.cop = []
        self.pr = []
        self.scn = []

    # @classmethod
    # def extract(cls, data):
    #     my_date = [i for i in data.split() if i != '-']
    #     return int(my_date[0]), int(my_date[1]), int(my_date[2])

    #    @staticmethod
    #    def valid(day, month, year):
    #
    #        if 1 <= day <= 31:
    #            if 1 <= month <= 12:
    #                if 2022 >= year >= 1900:
    #                    return f'Дата верна!'
    #                else:
    #                    return f'Год введен не правильно!'
    #            else:
    #                return f'Месяц введен не правильно!'
    #        else:
    #            return f'День введен не правильно!'
    #
    #    def __str__(self):
    #        return f'Введенная дата: {Data.extract(self.data)}'

    def add_to(self, equipment):
        self.dict.setdefault(equipment.name, []).append(equipment)

    def extract_1(self, name):
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)


class RoboHouse:

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.all_in_shop = []
        self.my_shop = []
        self.my_unit = {'Модель устройства: ': self.name, 'Цена: ': self.price, 'Количество: ': self.amount}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.amount}'

    def inter(self):
        while True:

            try:
                in_name = input(f'Введите наименование товара: ')
                in_price = int(input(f'Введите цену товара: '))
                in_amount = int(input(f'Введите количество товара помещаемого на склад: '))
                total = {'Модель устройства: ': in_name, 'Цена: ': in_price, 'Количество: ': in_amount}
                self.my_unit.update(total)
                self.my_shop.append(self.my_unit)
                print(f'Сейчас на складе: \n {self.my_shop}')

            except:
                return f'Вы ввели неккоректные данные, попробуйте еще раз'

            print(f'Завершить ввод -> Q, Продолжить -> Enter')
            q = input(f'---> ')
            if q == 'Q' or q == "q":

                self.all_in_shop.append(self.my_shop)
                print(f'Весь склад -\n {self.all_in_shop}')
                return f'Завершение сеанса'
            else:
                return RoboHouse.inter(self)


class Printer(RoboHouse):
    def __init__(self, series, name, price, amount):
        super().__init__(name, price, amount)
        self.series = series

    def action(self):
        return 'Печать документов'


class Scaner(RoboHouse):
    def __init__(self, name, price, amount_str):
        super().__init__(name, price, amount_str)
        self.scaner_dict = []

    def action(self):
        return 'Скан документов'


class Copier(RoboHouse):
    def __init__(self, name, price, amount, year):
        super().__init__(name, price, amount, year)
        self.xerox_dict = []

    def action(self):
        return 'Копирование документов'


test_1 = Printer(322, 'hp', 2000, 5)
sklad = Sklad()
print(test_1)
sklad.add_to(test_1)
print(test_1.inter())
scaner = Scaner('hp', '321', 90)
sklad.add_to(scaner)
print(sklad.dict)
sklad.extract_1('hp')
print(sklad.dict)
