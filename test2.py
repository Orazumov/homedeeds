#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} + i{self.y}'

    def __add__(self, other):
        return f'{self.x + other.x} + i{self.y + other.y}'

    def __sub__(self, other):
        return f'{self.x - other.x} + i{self.y - other.y}'

    def __mul__(self, other):
        return f'{self.x*other.x - self.y*other.y} + i{self.x*other.y + other.x*self.y}'

    def __truediv__(self, other):
        return f'{(self.x*other.x + self.y*other.y)/((other.x**2) + (other.y**2))} + i{(other.x*self.y - self.x*other.y)/((other.x**2) + (other.y**2))}'



number1 = Complex(5, 4)
print(number1)
number2 = Complex(2, 1)
print(number2)
print(number1 + number2)
print(number1 * number2)
print(number1 / number2)
print(number1 - number2)

