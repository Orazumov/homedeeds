# Начало ООП.

import statistics

# модуль считает медианы, среднее и т.д.
# все что нужно для статичтики.

statistics.mean() #считает среднее значение по списку.

# до появления С++ не было ООП, поэтому была проблематична скорость
# написания ПО. Сейчас используется повсеместно.

# можно описывать различные объекты с точки зрения высшей абстракции - как абстр.
# модель. Это позвол лучше контрол. код, лучше его развивать, исправл ошибки быстрее.
# Код более читаем. Не обязательно знать что творится в объекте, чтобы им пользоваться.
# Позволяет создавать абстракции, которые можно повторно исп. и поддерживать.

# Появляется наследование и инкапсуляция. Позволяет создавать новые объекты, наследуя
# свойства от др. объектов.

# Класс, объект, атрибут(метод) - 3 базовые понятия.

# Класс - это асбтракция, общие характеристики.
# Например, все автомобили - 3-8 колес, имеют цвет, двигатель электронику и т.д.

# Когда описываем конкретный автомобиль, мы задаем значения этим аттрибутам, работая по шаблону
# класса, описывая конечный объект.

# В Питон - все базовые типы - класс, даже ф. - класс.

# Классы начинаются с большой буквы, CamelCase.

# Описание человека как класс:

class Human:
    eye_color = None
    name = None
    skin_color = None

vasya = Human()

# Задаем переменные для объекта класса.
# переменные заперты внутри класса.

vasya.skin_color = 'Black'
vasya.eye_color = 'Red'
vasya.name = 'Вася'

# Но мы хотим сразу создавать Васю как объект. для этого нужен конструктор класса:

def __init__(self, name, eyes_color, body_color):

# self - ссылка на себя, общение с собой же.
# метод - ф. внутри класса.
    self.name = name
    self.eyes_color = eyes_color
    self.skin_color = skin_color
# теперь обязательно задавать атрибуты:

vasya = Human('Вася', 'Карие', 'Белый')

# добавим популяцию:

class Human:
    eye_color = None
    name = None
    skin_color = None
    population = 0

def __init__(self, name, eyes_color, body_color):

    self.name = name
    self.eyes_color = eyes_color
    self.skin_color = skin_color
    Human.population += 1

vasya = Human('Вася', 'Карие', 'Белый')

# после этого population стал 1.

vasya.population # 1

# можно убрать строки из класса:

class Human:
    population = 0

# переменные внутри класса - это аттрибуты, ф. внутри класса - это методы.

Human.population = 55

# теперь

vasya.population = 55

# Но если мы зададим ему отдельно, это распространится только на него, а на petr - нет.

petr = Human('Петя', 'Голубые', 'Черный')

# на него не распространится.

# сущ. и др. magic методы, такие как __init__ (конструктор, выполняется первым).

# добавил пол:

from random import choice

class Human:
    population = 0

def __init__(self, name, eyes_color, skin_color, sex):

    self.name = name   # переменная для всех экземпляров.
    self.eyes_color = eyes_color
    self.skin_color = skin_color
    self.sex = sex
    Human.population += 1

def breeding(self, other):
    if self.sex == other.sex:
        name = choice(['саша', 'женя']) # локальная переменная внутри метода
        sex = choice(['М', 'Ж'])
        return Human(name, choice([self.eye_color, other.eye_color]), self.skin_color, sex)


vasya = Human('Вася', 'Карие', 'Белый', 'М')
tanya = Human('Таня', 'Голубые', 'Черный', 'Ж')

child = vasya.breeding(tanya)

# рождается ребенок.
# ф. работает с внутренними параметрами объекта.

# модификаторы доступа:

#Private, Public, Protected.

# если бы мы написали:

class Human:
    _population = 0

def __init__(self, name, eyes_color, skin_color, sex):

    self.name = name   # переменная для всех экземпляров.
    self.eyes_color = eyes_color
    self.skin_color = skin_color
    self.sex = sex
    Human._population += 1 # protected

# эту переменную из внешнего кода не рекомендуется менять.
#(можно, но не надо).

class Human:
    __population = 0

def __init__(self, name, eyes_color, skin_color, sex):

    self.name = name   # переменная для всех экземпляров.
    self.eyes_color = eyes_color
    self.skin_color = skin_color
    self.sex = sex
    Human.__population += 1 # protected

# можно поменять только тут, извне - нет.

# есть обходные пути как можно поменять:

vasya._Human__population = 1

# можно инкапсулировать сами методы, чтобы другие не могли его менять.

# классы можно импортировать:
#from file import board
# можно импортировать даже переменные.

# наследование:

class Animal:
    def __init__(self, sex, kind):
        self.sex = sex
        self.kind = kind

    def say(self):
        print("ААУКУКА")

# будет наследовать от животного черты:

class Homo(Animal):
    def __init__(self, name, sex, kind):
        self.name = name
# только имя индивидуально, все остально наследуется.
        super().__init__(sex, kind) # передаем значения параметров в Animal.

vasya = Homo('Вася', 'М', 'HOMO')

# создали животных, а потом получился человек, который отличается именем.

vasya.say()
# ААУКУКА
# этот метод мы наследовали от "Animal"

# Полиморфизм.
# наследники могут иметь отличный вид:

class Homo(Animal):
    def __init__(self, name, sex, kind):
        self.name = name
        super().__init__(sex, kind)

    def say(self):
        print(f'Я есть {self.name}')

# перегрузка методов, сейчас будет исп. тот, который описан у Хомо6

vasya.say()

# может быть множественное наследование.

class Mechanics:
    def __init__(self, material):
        self.material = material

class Transport:
    def __init__(self, type):
        self.type = type

class Auto(Transport, Mechanics):
    def __init__(self, name, type, material):
        self.name = name
# нужно задать атрибуты для обоих родителей:
#        super().__init__(type=type, material=material)
# так не будет работать, т.к. нужно указать какому родителю что идет.
# поэтому делаем так:
        super().__init__(type=type) # всегда идет к первому родителю.
        # можно так: Transport.__init__(self, type)
        Mechanics.__init__(self, material) # это идет к конкретному родителю.

dodje = Auto('Чарджер', 'МаслКар', 'Железо')

# необычно работает полиморфизм:

class Mechanics:
    def __init__(self, material):
        self.material = material
    def hello(self):
        print('am Mech')

class Transport:
    def __init__(self, type):
        self.type = type
    def hello(self):
        print('am Transport')

class Auto(Transport, Mechanics):
    def __init__(self, name, type, material):
        self.name = name
        super().__init__(type=type)
        Mechanics.__init__(self, material)

dodje = Auto('Чарджер', 'МаслКар', 'Железо')

dodje.hello()  # am Transport,  т.к. не происходит переопределение атрибутов.
# наследуется сначала что есть, потом только то, чего ранее не было унаследовано.
# class Auto(Transport, Mechanics) <- тут главный класс транспорт! а не как написано выше.

#--------------------------------------------


dodje.__class__  # показывает к какому классу принадлежит этот объект.

dodje.__class__.__bases__ # показывает из какого класса наследует данный объект.

RightPyramid.__mro__ # смотрим в каком порядке алгоритм будет смотреть разные классы и в каком порядке брать параметры
# из них .


