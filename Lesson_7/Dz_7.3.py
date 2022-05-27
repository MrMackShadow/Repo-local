class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * "*"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательный результат!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity)) if (self.quantity // other.quantity) > 0 else print('Отрицательный результат!')

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cell1 = Cell(32)
cell2 = Cell(20)
print(f'1-ая клетка', cell1)
print(f'2-ая клетка', cell2)
print(f'Результат сложения двух клеток', cell1 + cell2)
print(f'Результат вычитания 1-ой клетки из 2-ой', cell2 - cell1)
print(f'Количество ячеек 2-ой клетки:', cell2.make_order(5))
print(f'Количество ячеек 1-ой клетки:', cell1.make_order(10))
print(f'Результат деления 1-ой клетки на 2-ю', cell1 / cell2)
