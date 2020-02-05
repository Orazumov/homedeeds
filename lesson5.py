# Работа с файлами.

# открываем файл. ф. open

data = 'этот текст надо записать в файл'

# режимы работы с файлами: r - read, w - write, b - binary в бинарном виде все содержимое.
# + мы можем комбинировать, т.е. bw, br, r+ (read + write)

file = open('temp.txt', 'w', encoding='UTF-8')  #после ф. open весь файл сразу в памяти, пока не закрыли его.
# кодировка не обязательный параметр, но лучше передать. сразу read нельзя, т.к. файла еше нет.
# файл появится по соседству с тем, откуда запускаем скрипт.

file.write(data) # записываем

file.close() # закрываем

# w - если файла нет, он создается, если есть, он перезаписывается.

# если хотим дозаписать файл:

file = open('temp.txt', 'a', encoding='UTF-8')

file.write(data+'\n') # записываем с переносом строки

file.close() # закрываем

# чтение из файла:

file = open('temp.txt', 'r', encoding='UTF-8')

new_data = file.read()

#new_data = file.read(количество байт, которые нужно считать)
# отсчет от того места где нах. курсов(виртуальный). Когда только открыли файл - он в начале,

file.close()

print(new_data)

# если бинарно:

data = b'Hello'

file = open('temp.txt', 'wb')

file.write(data)

file.close()

#русские символы :

data = bytes('русские буквы', encoding='UTF-8')

# потом это записываем в файл.

# в виде битов записываем например изображение.

file = open('temp.txt', 'rb')

new_data = file.read()

file.close()

print(new_data)

# будут биты вместо русских букв в hex.

# файл - итерируемый объект, поэтому мы можем делать так:
file = open('temp.txt', 'r')

for line in file:
    print(line)

file.close()

# будет печататься каждая строка, итератор проходит построчно.
# у принта тоже есть \n поэтому печатается 2 раза перенос коретки.

# сахар:
# контекстный менеджер закрывает файл, когда прекращается работа внутри with:

with open('temp.txt', 'r') as file: # назвали файл именем file
    for line in file:
        print(line)

# в бинарном виде нужно записывать любой нетекстовый формат (фото, пдф и т.д.).

import os.path
import sys

# формирование пути к файлу.

#есть путь относительный и абсолютный
# относительный - относительно того где находишься сейчас.
# в терминале без / в начале...
# чтобы точно знать местонахождение исп. полный путь.
# для этого исп. библ os.path
# полный путь будет начинаться с /
# c:\\ .. win
# /Volumes/c/ mac, linux
# pwd - узнать полный путь.

#sys.argv - первым арг. видим файл через кот. зап прилож.
# если python les5.py - параметр будет просто les5.py относ. если запускаем из командной строки скрипт.

import sys

print(argv)

#полный путь

import os

print(os.getcwd())

# путь в папке где лежит файл.

print(__file__)

# полный путь к файлу в котором выложен метод.

# формируем путь:

import os.path as path

# path.abspath(__file__) - путь к файлу

base_path = path.join(path.dirname(__file__), 'text.txt') # составляем с файлом в конце

# join склеивает путь.

print(base_path)

with open(base_path, 'w') as file:
    file.write(data)

# записали файл по пути.

# можно сделать по другому:

path.split(__file__)

# возвращается кортеж - сначала путь к директории, на втором месте имя файла.
# из нее можно сделать base_path

base_path = path.join(path.split(__file__)[0], 'text.txt')

import os.path as path

def my_func():
    base_path = path.join(path.split(__file__)[0], 'text.txt')
    print(base_path)
    return base_path

# импортировали в др проект и вызываем эту ф.
# путь будет относительно корня проекта.

import os.path as path
import sys

def my_func():
    base_path = sys.argv
    print(base_path)
    return base_path

# тогда после импорта в др. проект который находится в др. папке,
# отображается путь в той папке, из которой мы вызывли ф.

# если нам нужно узнать все что нах. в папке:

# смотрим текущую директорию. listdir = ls
print(os.listdir('.')) # . - текущее место положение.
print(os.listdir('..')) # на уровень выше.

# удаляем:

os.remove('text.txt')

# ошибка Operation not permitted, т.к.

os.remove('test/')

# мы хотим удалить папку, а в ней есть еще файл.
# но все равно фейл, т.к. os.remove удаляет только файлы. Это разные вещи.

os.rmdir('test/') # чтобы удалить папку.

for itm in os.listdir('test/test.txt'):
    if os.path.isfile(f'test/{itm}'):  # проверяем файл ли это
        os.remove(f'test/{itm}')

# если есть еще вложенности - не получится. нужно писать отдельные ф., которые все обходят и проверяют.

# Создаем папки.

os.mkdir('test3')

os.getcwd() # смотрим где курсор.

# но может быть нам нужно переместиться в др. место.

os.chdir('test')

os.getcwd()

# видим, что переместились в папку test.

# сущ. модуль shutil

import shutil

shutil.rmtree('test')

# в папке тест есть еще подпапки, но shutil с этим справляется.

shutil.copy('photo.jpg', 'test3') # что копируем, путь, куда копируем.

os.system('python test.py') # как будто запускаем скрипт питона из терминала.
# можем также запустить любое приложение, передать системную команду.
os.system('nano')

# формат json.

import json

data = {
    'key1': [1, 2, 3, 4],
    'key2': {'key3': 'data'},
    'key4': 'Данные'
}

# ХОТИМ передать данные, чтобы получивший обратно преобразовал их в словарь.

j_data = json.dumps(data)

print(j_data)
print(type(j_data))

# это строка. как бы словарь в виде строки.

with open('jdata.json', 'w') as file:
    file.write(j_data)

#Появился файл, куда записался словарь.
#как считать и обратно в словарь превратить?

with open('jdata.json', 'r') as file:
    j_data = file.read()

new_data = json.loads(j_data)

print(type(new_data))
print(new_data)

# снова стал словарем!
# но json поддерж. не все типы, он поддерж: None (= Nil), int, float, list, dict, (NOT tuple!), bool, str
# в json часто хранят состояние программ, какие-то простенькие бд.

# если либа ставится через PIP - исп. относ. пути.
# если работаем с путем внутри ПК, то полный путь, он более точный!









