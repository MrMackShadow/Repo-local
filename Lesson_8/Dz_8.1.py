class Data:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def extract(cls, data):
        my_date = [i for i in data.split() if i != '-']
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 1900:
                    return f'Дата верна!'
                else:
                    return f'Год введен не правильно!'
            else:
                return f'Месяц введен не правильно!'
        else:
            return f'День введен не правильно!'

    def __str__(self):
        return f'Введенная дата: {Data.extract(self.data)}'


data_today = Data('21 - 11 - 2015')
print(data_today)
print(data_today.valid(11, 11, 2022))
print(data_today.valid(1, 13, 2020))
print(data_today.valid(33, 12, 2020))
print(data_today.extract('11 - 11 - 2011'))
print(data_today.extract('11 - 11 - 2020'))
print(data_today.valid(1, 11, 2000))
