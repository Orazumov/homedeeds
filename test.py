# 7.Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджеры контекста.

import json

comp_dict = {}
benefit = 0

with open('companies.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(lines)
    for words in lines:
        print(words.split())
        comp_dict.update({words.split()[0]: (int(words.split()[2]) - int(words.split()[3]))})
        if int(words.split()[2]) > int(words.split()[3]):
            benefit = benefit + comp_dict[words.split()[0]]
final_list = [comp_dict, {'average_profit': f'{benefit/len(lines)}'}]

j_data = json.dumps(final_list)

with open('jdata.json', 'w') as file:
    file.write(j_data)

print(j_data)
