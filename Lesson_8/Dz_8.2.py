class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def zero(a, b):
        try:
            return (a / b)
        except ZeroDivisionError:
            return (f"Делить на ноль нельзя")


div = Division(12, 122)
print(div.zero(21, 0))
print(div.zero(10, 2))
