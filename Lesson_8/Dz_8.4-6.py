class Sklad:
    def __init__(self):
        self.dict = {}
        self.cop = {}
        self.pr = {}
        self.scn = {}

    def add_to(self, equipment):
        self.dict.setdefault(equipment.name, []).append(equipment)

    def add_to_cop(self, equipment):
        self.cop.setdefault(equipment.name, []).append(equipment)

    def add_to_pr(self, equipment):
        self.pr.setdefault(equipment.name, []).append(equipment)

    def add_to_scn(self, equipment):
        self.scn.setdefault(equipment.name, []).append(equipment)

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
        self.cop = []
        self.pr = []
        self.scn = []
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
                print(f'Весь товар на складе: \n {self.my_shop}')
                print(f'Отдел принтеров: \n {self.pr}')
                print(f'Отдел сканеров: \n {self.scn}')
                print(f'Отдел ксероксов: \n {self.cop}')
            except:
                return f'Вы ввели неккоректные данные, попробуйте еще раз'

            print(
                f'Завершить ввод -> Q, Перенести на склад Принтеров -> P, На склад сканеров -> S, Склад Ксероксов -> C  Продолжить -> Enter')
            q = input(f'---> ')
            if q != 'Q' or q != "q":
                if q != "p" or q != "P":
                    if q != "c" or q != "c":
                        if q != "s" or q != "S":
                            return RoboHouse.inter(self)
                        else:
                            return self.scn.append(self.my_shop)

                    else:
                        return self.cop.append(self.my_shop)
                else:
                    return self.pr.append(self.my_shop)
            else:
                self.all_in_shop.append(self.my_shop)
                print(f'Весь склад -\n {self.all_in_shop}')
                return f'Завершение сеанса'


class Printer(RoboHouse):
    def __init__(self, series, name, price, amount):
        super().__init__(name, price, amount)
        self.series = series


class Scaner(RoboHouse):
    def __init__(self, name, price, amount_str):
        super().__init__(name, price, amount_str)
        self.scaner_dict = []


class Copier(RoboHouse):
    def __init__(self, name, price, amount):
        print('Новый копировальный аппарат: ')
        super().__init__(name, price, amount)
        self.xerox_dict = []


printer = Printer(322, 'hp', 2000, 5)
scaner = Scaner('Lenovo', '321', 90)
sklad = Sklad()
print(printer)
print(scaner)
sklad.add_to(printer)
sklad.add_to_pr(printer)
print(sklad)
print(printer.inter())
sklad.add_to(scaner)
print(sklad.dict)
sklad.extract_1('hp')
print(sklad.dict)
