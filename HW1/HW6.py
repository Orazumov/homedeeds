#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep

class TrafficLight:

    __color = ('red', 'yellow', 'green')

    def running(self):

        order_as_is = []
        order_correct = ('red', 'yellow', 'green')
        for i in range(len(self.__color)):
            print(self.__color[i])
            order_as_is.append(self.__color[i])
            if order_as_is[i] != order_correct[i]:
                print('Порядок ошибочен!')
                return None
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(2)

TL1 = TrafficLight()
TL1.running()


#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
#Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    __lenght = 5000
    __width = 20

    def mass_count(self, mass_asfalt, high):
        self.mass_asfalt = mass_asfalt
        self.high = high
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна ({self.__width} * {self.__lenght} * {self.mass_asfalt} * {self.high}): {self.__width * self.__lenght * self.mass_asfalt * self.high}')

road1 = Road()
mass_asfalt = int(input('Введите массу асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см: '))
high = int(input('Введите число см толщины полотна: '))

road1.mass_count(mass_asfalt, high)

#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать
# данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    name = None
    surname = None
    position = None
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Общий доход сотрудника: {int(self._income["wage"]) + int(self._income["bonus"])}'

worker = Position('Oleg', 'Razumov', 'programmer', '70000', '10000')
print(worker._income)

print(worker.get_full_name())
print(worker.get_total_income())

#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#cоздайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import randint

class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print("Машина поехала!")

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print(f'Машина повернула на {direction}')

    def show_speed(self):

        print(f'Скорость машины: {self.speed + randint(5, 30)}')

class TownCar(Car):

    def show_speed(self):
        self.speed = self.speed + randint(5, 30)
        print(f'Скорость машины (из subclass TownCar): {self.speed}')
        if self.speed > 60:
            print('Превышение скорости 60 км/ч!')

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        self.speed = self.speed + randint(5, 30)
        print(f'Скорость машины (из subclass WorkCar): {self.speed}')
        if self.speed > 40:
            print('Превышение скорости 40 км/ч!')

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

car1 = WorkCar(30, 'yellow', 'Traktor')
car1.go()
car1.stop()
car1.turn('право')
car1.turn('лево')
car1.show_speed()

car2 = PoliceCar(90, 'blue', 'Lada Calina')
print(car2.is_police)
car2.show_speed()
print(car2.speed)
print(car2.name)

#5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки карандашом.')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки маркером.')

pen = Pen('Синяя ручка')
print(pen.title)
pen.draw()

pencil = Pencil('Простой карандаш')
print(pencil.title)
pencil.draw()

handle = Handle('Зеленый маркер')
print(handle.title)
handle.draw()


