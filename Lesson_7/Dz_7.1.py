class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        mat = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                mat[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))


result = Matrix([[5, 18, 11],
                 [6, 17, 23],
                 [41, 50, 9]],
                [[45, 8, 2],
                 [6, 7, 93],
                 [24, 5, 97]])

print(f'Результат cложения матриц: \n', result.__add__())
