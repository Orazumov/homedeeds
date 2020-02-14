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