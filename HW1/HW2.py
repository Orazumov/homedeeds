#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list_1 = [5, 'hello', True, 2.5, [1, 2], {5, 6, 9}, (4, 5, 6)]

i=0
while(i <= 6):
    print(type(list_1[i]))
    i +=1

#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

list_2 = []

number_elem_list = int(input('Введите количество элементов в списке: '))
n = 0

while n <= (number_elem_list - 1):
    list_2.append(input(f'Введите элемент списка {n}: '))
    n += 1

print('Исходный список', list_2)

m = 0

if len(list_2) % 2 != 0:
    last_element = list_2.pop()
else:
    last_element = 0

while m < len(list_2):
    list_2[m], list_2[m + 1] = list_2[m + 1], list_2[m]
    m = m + 2

if last_element:
    list_2.append(last_element)

print('Получили список: ', list_2)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_num = int(input('Введите порядковый номер месяца: '))

months_dict = {12: 'зима', 1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень'}

print(f'Решение через словарь: Вы ввели месяц номер {month_num}, это {months_dict[month_num]}')

list_months = [[12, 1, 2,  'зима'], [3, 4, 5, 'весна'], [6, 7, 8, 'лето'], [9, 10, 11, 'осень']]

for x in range(len(list_months)):
    for y in range(len(list_months[x])):
        if list_months[x][y] == month_num:
            index = [x, y]
        else:
            continue

print(f'Решение через список: Вы ввели месяц {month_num}, это {list_months[index[0]][3]}')

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

string = input('Введите строку из нескольких слов с пробелами: ')

number = 1
for z in (string.split()):
    if len(z) > 10:
        z = z[:10]
    print(f'{number}. {z}')
    number += 1

#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

natural_numbers = [7, 5, 3, 3, 2]

print('Изначальный рейтинг: ', natural_numbers)

for k in range(5):
    natural_numbers.append(int(input('Введите число для размещения в рейтинг: ')))

natural_numbers.sort(reverse=True)

print('Рейтинг после добавления введенных чисел: ', natural_numbers)

#6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#Пример готовой структуры:
#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]

item = []
items = []
items_analytics = []

for f in range(2):

    item = []
    items_char = []
    items_char_name = []
    items_char_price = []
    items_char_amount = []
    items_char_meas = []

    item.append(f)
    items_char_name.append('name')
    items_char_name.append(input(f'Введите название товара {f}: '))
    items_char.append(items_char_name)
    items_char_price.append('price')
    items_char_price.append(input(f'Введите цену товара {f}: '))
    items_char.append(items_char_price)
    items_char_amount.append('amount')
    items_char_amount.append(input(f'Введите количество товара {f}: '))
    items_char.append(items_char_amount)
    items_char_meas.append('measure')
    items_char_meas.append(input(f'Введите ед. изм. товара {f}: '))
    items_char.append(items_char_meas)


    items_char = dict(items_char)
    item.insert(f+1, items_char)
    item = tuple(item)
    items.insert(f, item)

    items_analytics.append(items_char)



print('Структура данных "Товары": ', items)

#Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.
#Пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}

items_analytics_result = []
items_analytics_result_name = []
items_analytics_result_price = []
items_analytics_result_amount = []
items_analytics_result_measure = []

for q in range(len(items_analytics)):
    items_analytics_result_name.append(items_analytics[q].get('name'))
    items_analytics_result_price.append(items_analytics[q].get('price'))
    items_analytics_result_amount.append(items_analytics[q].get('amount'))
    items_analytics_result_measure.append(items_analytics[q].get('measure'))

items_analytics_result = {'название': items_analytics_result_name, 'цена': items_analytics_result_price, 'количество': items_analytics_result_price, 'ед. изм': items_analytics_result_measure}

print('Аналитика: ', items_analytics_result)















