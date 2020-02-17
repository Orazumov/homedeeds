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


#6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.



