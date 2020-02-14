#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать
# данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц вы найдете в методичке.
#Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым
# элементом первой строки второй матрицы и т.д.

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
        return f'{self.matrix}'
    #return '\n'.join(map(lambda st: ' '.join(map(str, st)), self.matrix))

    def __add__(self, other):

        matrix_zip = list(zip(self.matrix, other.matrix))
        matrix_sum = []

        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):

            for i in range(len(self.matrix)):
                matrix_sum.append(list(map((lambda x, y: x + y), matrix_zip[i][0], matrix_zip[i][0])))
            return matrix_sum

        else:
            print('Складывать можно только матрицы одной размерности!')
            return None

matrix1 = Matrix()
matrix2 = Matrix()
print(matrix1)
print(matrix2)
matrix3 = matrix1 + matrix2
print(matrix3)

#2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике работу декоратора @property.

# Вариант с одним классом:

from abc import ABC, abstractmethod

class AbcClothes(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def amount(self):
        pass

class Clothes(AbcClothes):

    def __init__(self):

        while True:
            type = int(input('Введите тип одежды: Пальто - 1, костюм - 2: '))
            if type == 1:
                self.type = 'Coat'
                break
            elif type == 2:
                self.type = 'Costume'
                break
            else:
                print('Выберите 1 или 2')
        self.name = input('Введите название модели: ')

    def __add__(self, other):
        return (f'Общий расход ткани: {self.amount + other.amount}')

    @property
    def parameters(self):
        return self.size

    @parameters.setter
    def parameters(self, size):
        self.size = size
        return self.size

    def amount(self):

        if self.type == 'Coat':
            self.amount = self.size // 6.5 + 0.5
            return (f'Расход ткани на пальто {self.size // 6.5 + 0.5} м')

        elif self.type == 'Costume':
            self.amount = 2 * self.size + 0.3
            return (f'Расход ткани на костюм {2 * self.size + 0.3} м')

cloth1 = Clothes()
cloth2 = Clothes()
print(cloth1.type)
print(cloth1.name)
print(cloth2.type)
print(cloth2.name)
cloth1.parameters = 52
cloth2.parameters = 180
print(cloth1.parameters)
print(cloth2.parameters)
print(cloth1.amount())
print(cloth2.amount())
print(cloth1 + cloth2)

# Вариант с двумя классами:

from abc import ABC, abstractmethod

class AbcClothes(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def amount(self):
        pass

class Coat(AbcClothes):

    def __init__(self):

        self.name = input('Введите название модели: ')

    def __add__(self, other):
        return (f'Общий расход ткани: {self.amount + other.amount}')

    @property
    def parameters(self):
        return self.size

    @parameters.setter
    def parameters(self, size):
        self.size = size
        return self.size

    def amount(self):

        self.amount = self.size // 6.5 + 0.5
        return (f'Расход ткани на пальто {self.size // 6.5 + 0.5} м')


class Costume(AbcClothes):

    def __init__(self):

        self.name = input('Введите название модели: ')

    def __add__(self, other):
        return (f'Общий расход ткани: {self.amount + other.amount}')

    @property
    def parameters(self):
        return self.size

    @parameters.setter
    def parameters(self, size):
        self.size = size
        return self.size

    def amount(self):

        self.amount = 2 * self.size + 0.3
        return (f'Расход ткани на костюм {2 * self.size + 0.3} м')


cloth1 = Coat()
cloth2 = Costume()

print(cloth1.name)

print(cloth2.name)
cloth1.parameters = 52
cloth2.parameters = 180
print(cloth1.parameters)
print(cloth2.parameters)
print(cloth1.amount())
print(cloth2.amount())
print(cloth1 + cloth2)

#3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение
# (add()), вычитание (sub()), умножение (mul()), деление (truediv()).Данные методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
#Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить
# соответствующее сообщение.
#Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
#Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование
# ряда не хватает, то в последний ряд записываются все оставшиеся.
#Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: **\n\n.
#Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: **\n\n***.
#Подсказка: подробный список операторов для перегрузки доступен по ссылке.

from random import randint

class Cell:

    def __init__(self):
        self.number = randint(1, 10)

    def __add__(self, other):
        return (self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return self.number - other.number
        else:
            print('Невозможно, количество клеток получится меньше 0.')

    def __mul__(self, other):
        return self.number*other.number

    def __truediv__(self, other):
        return self.number//other.number

    def make_order(self, number):
        full_stars = ''
        for i in range(number):
            if (i+1)%5 == 0:
                full_stars = full_stars + '*\n'
            else:
                full_stars = full_stars + '*'

        print(full_stars)

Cell1 = Cell()
print(Cell1.number)
Cell2 = Cell()
print(Cell2.number)
Cell3 = Cell()
Cell3.number = Cell1 + Cell2
print(Cell3.number)
Cell3.make_order(Cell3.number)




