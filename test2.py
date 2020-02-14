class Matrix:

    def __init__(self):
        self.matrix = []

        m = int(input('Введите размерность матрицы m: '))
        n = int(input('Введите размерность матрицы n: '))

        for i in range(m):
            self.matrix.append([])
            for j in range(n):

                while True:
                    try:
                        self.matrix[i].append(int(input(f'Введите число матрицы m*n с индексом {i} - {j}: ')))
                        break
                    except ValueError:
                        print('Введите число!')
                        continue

    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        #return f'{self.matrix}'
        return '\n'.join(map(lambda st: ' '.join(map(str, st)), self.matrix))

    def __add__(self, other):

        matrix_zip = list(zip(self.matrix, other.matrix))
        matrix = []

        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):

            for i in range(len(self.matrix)):
                matrix.append(list(map((lambda x, y: x + y), matrix_zip[i][0], matrix_zip[i][0])))
            return matrix

        else:
            print('Складывать можно только матрицы одной размерности!')
            return None

matrix1 = Matrix()
matrix2 = Matrix()
print(matrix1)
print(matrix2)
matrix3 = matrix1 + matrix2
print(matrix3)