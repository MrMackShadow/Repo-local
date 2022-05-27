class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма {self.a, self.b} и {other.a, other.b} = ({self.a + other.a} + {self.b + other.b})'

    def __mul__(self, other):
        return f'Произведение {self.a, self.b} и {other.a, other.b} = ({self.a * other.a - (self.b * other.b)} + {self.b * other.a})'

    def __str__(self):
        return f'Число {self.a} & {self.b}'


number_1 = Numbers(3, 5)
number_2 = Numbers(-8, -2)
print(number_1)
print(number_2)
print(number_1 + number_2)
print(number_1 * number_2)