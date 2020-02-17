#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:

    date = ''
    day = None
    month = None
    year = None

    def __init__(self, date: str):
        Date.date = date

    @classmethod
    def to_int(cls):
        Date.day, Date.month, Date.year = (Date.date.split('-'))
        Date.day = int(Date.day)
        Date.month = int(Date.month)
        Date.year = int(Date.year)
        print(f'Введенная дата: {Date.date} разбита на отдельные числа типа int.')

    @staticmethod
    def check():
        if Date.day < 1 or Date.day > 31:
            print('Введено неверное число! ', Date.day)
        elif Date.month < 1 or Date.month > 12:
            print('Введен неверный месяц!', Date.month)
        elif Date.year < 1:
            print('Введен неверный год!', Date.year)
        else:
            print('Дата введена верно!')


date1 = Date('0-07-1983')
Date.to_int()
Date.check()

date1 = Date('15-07-1983')
Date.to_int()
Date.check()

#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class OwnErrorClass(Exception):
    def __init__(self, txt='Деление на ноль запрещено!'):
        self.txt = txt
        print(self.txt)

a_number = int(input("Введите делимое: "))
b_number = int(input("Введите делитель: "))

if b_number == 0:
    error = OwnErrorClass()
# хотя логичнее было бы сделать raise OwnErrorClass.. но написано, что ошибки быть не должно.
else:
    c_number = a_number/b_number
    print(f"Результат деления: {c_number}")

#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
#Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class Number_check(Exception):

    element = None

    def check(self, element):
        Number_check.element = element
        if Number_check.element.isdigit():
            return Number_check.element
        else:
            print('Введите число!')
            return False

list = []

while True:

    element1 = input('Введите элемент списка. Для завершения введите stop: ')
    if element1 == 'stop':
        break
    number = Number_check()
    if number.check(element1):
        list.append(number.check(element1))

print(list)

#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
# будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
# классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
# каждого типа оргтехники.

class Storage:

    def __init__(self, name):

        self.name = name

        self.box = []

    def add_item(self, object):     # добавляем объект (технику) на склад - список словарей.
        list = []
        string = str(object)
        list = string.split(' ')
        class_name = (str(object.__class__)).split('.')[1].split("'")[0]
        self.box.append({'class': class_name, 'name': list[0], 'number': int(list[1]), 'location': 'sklad'})

    def give_item(self, name, number, location):    # отдаем объект (технику) со склада в какое-то подразделение.
        for i in self.box[:]:
            if i['name'] == name and i['location'] == 'sklad':
                if i['number'] == number:
                    i['location'] = location
                else:
                    left_number = int(i['number']) - number
                    if left_number <= 0:
                        print('Нет доступной техники на складе.')
                        break
                    i['number'] = left_number
                    self.box.append({'class': i['class'], 'name': name, 'number': number, 'location': location})
            else:
                print('Проверьте правильность ввода.')
        sklad.minimize(name, location)  # sklad.minim... имя склада хард код, можно это легко изменить, но в данном случае предусмотрен 1 склад.

    def take_item(self, name, number, location):    # возвращаем объект (технику) на склад.
        for i in self.box[:]:
            if i['name'] == name and i['location'] == location:
                if i['number'] == number:
                    i['location'] = 'sklad'
                else:
                    left_number = int(i['number']) - number
                    i['number'] = left_number
                    self.box.append({'class': i['class'], 'name': name, 'number': number, 'location': 'sklad'})
        sklad.minimize(name, 'sklad')   # имя склада хард код, можно это легко изменить, но в данном случае предусмотрен 1 склад.

    def minimize(self, name, location):   # если есть элементы в списке с одинаковыми именами и местоположениями - схлопываем их в 1 элемент.
        count = 0
        indexes = []
        total_number = 0
        for i in range(len(self.box)):
            if self.box[i]['name'] == name:
                if self.box[i]['location'] == location:
                    count += 1
                    indexes.append(i)
        if count > 1:
            first_index = indexes.pop(0)
            total_number = self.box[first_index]['number']
            for z in indexes:
                total_number = total_number + self.box[z]['number']
                self.box.remove(self.box[z])
            self.box[first_index]['number'] = total_number
            count = 0
            indexes = []
            total_number = 0
        else:
            count = 0
            indexes = []
            total_number = 0

    def __getitem__(self, item):
        return self.box[item]

    def __iter__(self):
        return self.box.__iter__()

class OfficeEquipment:

# units - количество ячеек на складе.

    def __init__(self, name, number, weight, units):
        self.name = name
        self.number = number
        self.weight = weight
        self.units = units

class Printer(OfficeEquipment):

    def __init__(self, name, number, weight, units, color, printSpeed, type):
        super().__init__(name, number, weight, units)
        self.color = color
        self.printSpeed = printSpeed
        self.type = type

    def __str__(self):
        return f'{self.name} {self.number} {self.weight} {self.units} {self.color} {self.printSpeed} {self.type}'

class Scanner(OfficeEquipment):

    def __init__(self, name, number,  weight, units, color, resolution):
        super().__init__(name, number,  weight, units)
        self.color = color
        self.resolution = resolution

    def __str__(self):
        return f'{self.name} {self.number} {self.weight} {self.units} {self.color} {self.resolution}'

class Xerox(OfficeEquipment):

    def __init__(self, name,  number, weight, units, resourse, copySpeed):
        super().__init__(name, number, weight, units)
        self.resourse = resourse
        self.copySpeed = copySpeed

    def __str__(self):
        return f'{self.name} {self.number} {self.weight} {self.units} {self.resourse} {self.copySpeed}'


#5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

#6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# создали склад.
# склад предусмотрен 1.

sklad = Storage('Sklad1')

# создали объекты/технику.

HP = Printer('HP', 7, 35, 3, 'white', 50, 'laser')
HP_250 = Printer('HP_250', 5, 30, 2, 'white', 40, 'laser')
Epson = Scanner('EPSON', 1, 20, 1, 'creme', 600)
Epson_300 = Scanner('EPSON_300', 2, 25, 1, 'creme', 1200)
Xerox_20 = Xerox('XEROX_20', 3, 20, 2, 1000000, 50)
Xerox_50 = Xerox('XEROX_50', 1, 22, 2, 1000000, 60)

list_tech_dict = {'hp': HP, 'hp_250': HP_250, 'epson': Epson, 'epson_300': Epson_300, 'xerox_20': Xerox_20, 'xerox_50': Xerox_50}

print(f'Техника в наличии: {HP}, {HP_250}, {Epson}, {Epson_300}, {Xerox_20}, {Xerox_50}')

print('Чтобы добавить технику на склад, введите: add-name')
print('Чтобы перенести технику СО СКЛАДА в другое подразделение, введите: move-name-number-department')
print('Чтобы вернуть технику на склад, введите: return-name-number-location (откуда возвращаем)')
print('Для завершения работы введите: exit')

while True:             # ввод и парсинг данных.
    answer = input('Введите ваши действия: ')
    if answer == 'exit':
        break
    else:
        list_answer = answer.split('-')
        if list_answer[0] == 'add':
            for u in list_tech_dict.keys():
                if u == list_answer[1].lower():
                    sklad.add_item(list_tech_dict[u])
        elif list_answer[0] == 'move':
            try:
                sklad.give_item(list_answer[1].upper(), int(list_answer[2]), list_answer[3])
            except ValueError:
                print('Проверьте правильность ввода.')
                continue
            except IndexError:
                print('Проверьте правильность ввода.')
                continue
        elif list_answer[0] == 'return':
            try:
                sklad.take_item(list_answer[1].upper(), int(list_answer[2]), list_answer[3])
            except ValueError:
                print('Проверьте правильность ввода.')
                continue
            except IndexError:
                print('Проверьте правильность ввода.')
                continue
        else:
            print('Проверьте корректность ввода и введите действие еще раз.')
        print('*' * 30)
    for i in range(len(list(sklad))):
        print(sklad[i])

#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

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