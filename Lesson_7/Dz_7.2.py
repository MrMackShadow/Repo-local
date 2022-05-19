class Сlothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def get_square_c(self):
        return self.v / 6.5 + 0.5

    def get_square_j(self):
        return self.h * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани состовляет: {(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)} метров')


class Suit(Сlothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_c = round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f'На пальто нужно {self.square_c} метра ткани'


class Jacket(Сlothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_j = round(self.h * 2 + 0.3)

    def __str__(self):
        return f'На костюм нужно {self.square_j} метра ткани'


suit = Suit(2, 4)
jacket = Jacket(1, 2)

print(suit)
print(jacket)
print(suit.get_sq_full)
