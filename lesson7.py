# избегайте повторений, в этом смысле всегда исп. цикл.

# magic методы. перегрузка операторов.

class Auto:
    def __init__(self):
        pass
# мы не наследуем, но наследовагие авт. от класса object.
# тоже самое что:

class Auto(object):
    def __init__(self):
        pass
# init берется именно от object.

class Auto:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model
# self.brand - атрибут класса, = brand - это  локальная переменная в Auto.
# self.freferf можно менять.
# мы изменили init - перегрузка операторов, он уже был, мы дали ему новые ф.

ford = Auto('Ford', 'Red', 'Mustang')

#print(ford) -> описание типа объект по памяти такой-то
# хотелось бы чтобы он печатался нормально, есть метод:
    def __str__(self):
        return f'{self.brand} {self.color} {self.model}'

# переопределили метод str и теперь при:

print(ford) #выдасться f строка.

# управляем сбоощиком мусора:

    def __del__(self):
        print(f'Crash {self.model}')

# после того как выполнены все команды, запускается сборщик мусора и удаляет объекты.
# поэтому теперь после выполнения программы напечатается f строка.
# при этом все равно память очиститься, т.к. del выполняется уже после чистки.

class Garage:
    def __init__(self, name):
        self.name = name
        self.__box = []

    def add_auto(self, auto):
        self.__box.append(auto)

# box - то что стоит в гараже.

garage = Garage('Monkey')

garage.add_auto(ford)

# хотели бы обращаться к авто, смотреть на каком месте кто стоит.
# по индексу.
# garage[1] и распечатать.
# есть метод getitem

class Garage:
    def __init__(self, name):
        self.name = name
        self.__box = []

    def add_auto(self, auto):
        self.__box.append(auto)

    def __getitem__(self, item):
        return self.__box[item]

print(garage[0]) # работает!
# getitem вызывавется когда исп. [] у объекта.

class Human:

    def __init__(self, name):
        self.name = name

h1 = Human('Вася')
h2 = Human('Маша')

# хотим чтобы h3 = h1 + h2

    def __add__(self, other):
        return Human('Анатолий')

print(h3.name) # сработало! появился 3й человек.
# для сложения, вычитания, обр. через скобочки, вызова как ф., для всего есть magic
# методы, которые к тому же можно переопределить.
# некоторые ф. не заполнены по умолчанию, некоторые работают как-то стандартно.

h3 = h1.__add__(h2)

# можно вызвать так.

for car in garage:
    print(car)

# будет работать, т.к. есть getitem.
# но такой подход не оч. хорош:

def __iter__(self):
    return self.__box__.__iter__()
#потеряли возм. обр через индекс (если убрать __getitem__), но объект теперь итерируемый

# защищаем box, но извне чтобы можно было смотреть что в нем:

def box(self):
    return tuple(self.__box)

print(garage.box())
# внутри список объектов в памяти.

# хотим, чтобы было обр без вызова: garage.box
@property
def box(self):
    return tuple(self.__box)

print(garage.box)

# хотим чтобы можно было происваивать что-то нашему атрибуту:

@property
def box(self):
    return tuple(self.__box)

@box.setter
def box(self, other):
    self.__box.append(other)

garage.box = ford

# абстрактные методы:

from abc import ABC, abstractmethod
# абстрактный класс
class Animal(ABC):
    @abstractmethod
    def say(self):
        pass
    @abstractmethod # абс. метод.
    def born(self):
        pass

class Wolf(Animal):

    def __init__(self, name):
        self.name = name

# работать класс не будет, т.к. у нас есть суперкласс, который говорит что д.б.
# методы say и born
    def say(self):
        print('ERGER')

    def born(self):
        print('born')

# задаем интерфейс и все наследники точно будут иметь методы которые нужно.
# чтобы другой человек был обязан задать данные методы.
# абстрактный класс - это жесткие рамки для дальнейшей разработки.

class Funns:
    @staticmethod
    def my_funk():
        print('Hello')

# больше не нужен селф, т.к. метод работает без объекта.
# это статичная ф. для нашего класса.

#можно обр. без экземпляра класса:

Funns.my_funk()

# это группировка ф. внутри класса. полностью не зависят от экземпляра.
# можно импортировать класс Funns, а из него импорт. эту ф. как будто она независимая.

# вернемся в гараж:
class Auto:
    def __init__(self, brand, color, model, vin = None):
        self.brand = brand
        self.color = color
        self.model = model
ford = Auto('Ford', 'Red', 'Mustang', 'fewf')
chevi = Auto('Chevralet', 'Red', 'vsrvr', 'fewfwe')
tesla = Auto('Tesla', 'Red', 'Mustang')

garage.box = ford
garage.box = chevi
garage.box = tesla

for car in garage:
    print(car)

# хотелось бы иметь др. объект итератор:

class GarageIter:
    def __init__(self, cars):
        self.__cars = cars

# чтобы с ним работал for:

# цикл фор это:

tmp = garage.__iter__()
while True:
    try:
        car = tmp.__next__()
        print(car)
    except StopIteration:
        pass

# фор дергает next пока не встретит StopIteration.

class GarageIter:
    def __init__(self, cars):
        self.__cars = cars
        self.i = 0
        # переопределим next:
    def __next__(self):
        while True:
            if self.__cars[self.i].vin:
                self.i +=1
                return self.__cars[self.i-1]
                # не наоборот - иначе после return - выход из ф.
            self.i +=1
            if len(self.__cars) -1  < self.i:
                raise StopIteration
    # отдаваться будут машины только с vin кодом.

def __iter__(self):
    return GarageIter(self.__box)

# распечатаются только машины с vin кодом.
# интерфейс итератора состоит из метода next с ошибкой StopIteration.
# можно задать что возвращает итератор. Например мы задали так, чтобы возвр. только с vin кодом.
# д.б. еще __iter__ ! указано выше.

# простой шаблон проектирования - фабрика:

class Fabric:

    def __init__(self, name, count):
        self.name = name
        self.box = [Auto(self.name, 'Color' , 'Model', num) for num in range(count) ]

# num - это будет vin код.
# фабрика создает n количество объектов по шаблону.

ford_f = Fabric('ford', 20)
# получилась фабрика, где в боксе 20 фордов.

class Fabric:

    def __init__(self, name, count):
        self.name = name
        self.count = count
        self.prefix = 1

    def create(self, color):
        self.prefix += 1
        return [Auto(self.name, 'Color' , 'Model', f'{self.prefix}_{num}') for num in range(count) ]

ford_f = Fabric('ford', 20)
part = ford_f.create('Green')

# теперь фабрика создает еще и машины с цветом и по другому определяет vin код.
# заказывая партию, задаем еще и какой-то параметр.
# фабрика часто исп. в магазинах. Например, приходит товар - майка, но 1 000 000 шт.


