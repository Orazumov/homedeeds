# Урок номер 8.

# способы установки сторонних библиотек.

# концепция API = описание какие запросы можно сделать на опред. URL и что получить в ответ.
# рассматривается на примере GitHub Rest API.

# установка сторонних пакетов можно с github или с pip:
# в терминале: pip install - имя пакета.

# > pip install requests

# все, теперь библиотека доступна для импорта.

import requests

# хороший тон - в корне проекта файл: requirements - зависимости.
# > pip freeze > requirements.txt

# Установить все, что есть в файле:
# > pip install -r requirements.txt
# так может поступить другой человек, который будет читать ваш проект.
# чтобы у него он норм работал.

# метод get и URL из описания API:

url = 'https:...'
data = requests.get(url)
# приходит ответ.
# чтобы посмотреть ответ целиком запускаем дебаг и пишем:
print(1) # и на нем ставим брейкпоинт (красный шарик).
# если распечатать просто data, то будет Response [200]

data.text #- текст ответа.
data.status_code #- посмотреть что ответ нормальный.

data.json()
# получаем ответ в виде словаря json.

# паттерны проектирования.

class GithubUser:
    def __init__(self, **kwargs):
        pass

# мы хотели бы чтобы все пришедшие по ссылке атрибуты не описывались, а просто кидать в класс json, и получать ответ с атрибутами.

class GithubUser:
    def __init__(self, **kwargs): #**kwargs - это словарь.
        for key, value in kwargs.items():
            setattr(self, key, value)

url = 'https://api.github.com/users/gefmar'
data = requests.get(url)
gu = GithubUser(**data.json())

#теперь можем обращаться:

# gu.url
# gu.name
# gu.login
# и т.д.

# wrapper:

class Test:
    def __init__(self, args):
        self.__args = args

    def __getattr__(self, item):
        return getattr(self.__args, item)

# когда обращаемся .blabla - обр к методу и blabla - всегда перед в виде аргумента.

test = Test([2,3,4,5])

test.pop()
# удалился последний элемент. Этот подход - делегирование.

class Test:
    def __init__(self, args, kwargs):
        self.__args = args
        self.__kwargs = kwargs

    def __getattr__(self, item):
        try:
            return getattr(self.__args, item)  # сначала пытаемся сделать для списка, но список не поддерж update
        except AttributeError:
            return getattr(self.__kwargs, item)  # пробуем это сделать в словаре, получается.

test = Test([2, 3, 4, 5], {888: 999})

test.update({1: 2})

# делегирование.

# Например мы ждем от пользователя, что он пришлет нам строку.
# если строка менее 10 символов, выкидываем ошибку (например, пароль).

class ShortPasswordError(Exception):
    def __init__(self, text='Пароль короткий'):
        self.text = text

    def __str__(self):
        return self.text

# путь пользователь ввел пароль:
pwd = 'password'

if len(pwd) < 10:
    raise ShortPasswordError
# вышла ошибка как и было описано выше.
# можно : raise ShortPasswordError('произвольный текс') - вышла бы ошибка с произвольным текстом.from

# декораторы. нам известны @property, @statismethod.

class Temp:
    classname = 'TEMP'
    def __init__(self, name):
# сущ. методы самого класса - класс методы. он будет не в контексте экз класса, а в контексте самого класса.
        self.name = name

    @classmethod
    def test(cls, name):
        return cls(name)  # вместо Temp(name)

#метод New.

class Single:
    __instance = None

    def __init__(self):
        self.name = 'СИНГЛ'

    def __new__(cls, *args, **kwargs):   # отвечает за создание экз. класса, прежде чем отработает init.
        if not cls.__instance: # если экз. класса нет, тогда создаем новый экз. класс.
            cls.__instance = super(Single, cls).__new__(cls)
        return cls.__instance # в результате создается объект.

a = Single() # первый раз создается объект, т.к. instanse еще нет.
b = Single() # тут инстанс есть, возвращ один и тот же объект.
# сколько бы экз не создавали, всегда возвр. один и тот же объект.

# у всего есть имя.

def my_test(a,b):
    return a + b

# хотим логировать:

def deco(funk):
    def wrap(*args, **kwargs):
        print(funk.__name__)
        print(args, kwargs)
        return funk(*args, **kwargs)
    return wrap
@deco   # задекорировали ф. нашим декоратором.
def my_test(a,b):
    return a + b

my_test(2,3)   # напечаталось имя и аргементы, потом можно писать в файл.
# args и kwargs чтобы можно было исп. и имен и позиц аргументы.

# мы можем написать класс, который можно исп. как ф.

class Funk:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __sum(self):
        return self.a + self.b
# создаем перем:
test = Funk(3, 5)

test()
# нельзя, но если добавим:

class Funk:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __sum(self, *args):
        return self.a + self.b + sum(args)

    def __call__(self, *args, **kwargs):
        return self.__sum(*args)

print(test(1, 2, 3, 3)) # 17
# теперь это класс, но это callable элемент и его можно исп. как ф.

# Устанавливаем виртуальное окружение:

#> pip3 install virtualenv
#> python3 -m venv venv2
#> далее активируем:
# находимся в папке проекта:
# Scripts\activate win
# source venv2/bin/activate  mac, linux

# нужно если у нас есть проект, который работает с др. версией питона и др. библиотеками, чтобы у себя ничего не менять, создаем вирт окр.
# декативация: deactivate

# venv и venv2 полностью независимы друг от друга и от глобального интерпретатора.
# если нет либ, ставим их, например из requirements.txt (см. выше).



