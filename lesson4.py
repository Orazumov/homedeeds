# решение возведение через степень:
# x ** y = (x+x+x... х раз) + (x+x+x... х раз) ... y раз


new_func(2,3)

def my_multiply(x,y):
    result = 0
    for _ in range(y): # для дробных чисел, переписать на while и сделать корректировку.
        result +=x
    return result

def my_func(x,y):
    result = 1
    for _ in range(abs(y)):
        result = my_multiply(result, x)
    return result if y > 0 else 1 / result

# запилили отдельную ф. для умножения.
# лучше строки не складывать, лучше использовать ''.join(map(int_func, string,split(' ')))

# стандартная библиотека Python обладает широким ф., эти ф. нужно только импортировать.
# но некоторые библоитеки необходимо импортировать из др. мест.

# библиотека содержит модули, а модуль - это какая-то ф.

import random

# в нашей области видимости появилась ссылка на модуль random.

print(random.random()) # дает float число < 1 каждый раз новое.

print(random.randint(1, 100))
# от 1 до 100

tmp = [1,2,4,3,2,5]
print(random.shuffle(tmp)) # None
print(tmp) # сам объект изменился! перемешала числа.
# принимает в себя последовательность и изменяет ее.

# можно импортировать еще так:

from random import shuffle

# импортировали отдельную ф.

print(shuffle(tmp)) # незачем теперь писать random.

# но может возникнуть коллизия имен, если создадим тоже ф. shuffle.

from random import shuffle as rand_shuffle

# придали другое имя, чтобы не было конфликта. или чтобы по короче запись была.

from random import (shuffle,
                    randint,
                    randrange,
                    )
# хороший тон писать так.

from random import *
# так делать не хорошо. ее используют не часто!
# после этого пишем в коде:

randint(11)

shuffle(tmp)

# после этого убираем звездочку и прописываем все ф. вместо нее, PyCharm сам все подчеркивает.
# импорт принято делать в начале кода.

from functools import reduce

# нужно для

# например у нас есть код:
print(((((1+2) + 4) + 3) + 2) + 5)

tmp = [1, 2, 4, 3, 2, 5]

print(reduce(lambda x, y: x+y, tmp))

# результат тот же.

def print_log(level:str, data:str):
    print(f'{level}: {data}')

log_error = partial(print_log, 'ERROR')
log_info = partial(print_log, 'INFO')

log_error('Вызов ошибки') # ERROR: Вызов ошибки

from itertools import cycle

# пусть нам нужно бесконечно ходить по списку:

for itm in cycle(tmp):
    print(itm)

# будем ходить по круму по tmp.

from itertools import count

for itm in count(8, 3):
    print(itm)

# итератор идет начиная с 8 до бесконечности. 3 - шаг.

range (start, stop, step) # примерно тоже самое, только тут есть конец.

# float('inf') - бесконечность

# import math - для математических ф.

# как ставить библиотеки:

#для установки пользуемся pip

#команда в терминале:

#pip install numpy

# если создали свой модуль:

form my_module.module_one import my_func

# если создали папку my_module, в ней файл module_one, в нем ф. my_func

form .module_one import my_func
# если из той же директории файл.

# если в терминале:

python les4.py

#говорим интерпретатору что нужно запустить наш файл.

from sys import argv

python les4.py 123 132 777

print(argv)

#в строке сначала - относ путь к файлу, потом уже наши аргументы:

есть 2 ф. tmp, tmp2

funcs = {
    'one': tmp,
    'two': tmp2,
}

args = argv

func = funcs[args[1]]
x, y = args[2:4]
print(func(int(x), int(y)))

# получая агрументы, вызваем ф. с нужными параметрами и выполняем ее.

python les4.py one 132 777

import sys
sys.platform
'win32'

import os
os.name
'nt'

#import shutil - удобная работа с файлами и папками.

# генераторы списков:

tmp_list = [itm for itm in range(0, 20) if itm % 2]
print(tmp_list)
#[-> нечетные элементы с 0 дл 20].

# если есть еще ф.:

def tmp(x):
    return x/3

tmp_list = [tmp(itm) for itm in range(0, 20) if itm % 2]
print(tmp_list)

# [тоже только деленное на 3]

# тоже со словарем:
tmp_dict = {key: tmp(value) for key, value in {'key1':22, 'key2':33}.items() if value%2}

# генератор (настоящий!):

def my_gen(a,b):
    while a < b:
        yield a # return и не return. ф. на паузе, выходит из ф., выполн след код и снова в ф. отдает результат и дальше продолжает выполнение ф.
        a += 1

list(my_gen(1,5))





