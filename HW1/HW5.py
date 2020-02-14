#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('temp.txt', 'w', encoding='UTF-8') as file:
    while True:
        data = ''
        data = input('Введите строку для записи в файл. Если нужно прекратить ввод, ничего не вводите и нажмите Enter. ')
        if data == '':
            break
        else:
            file.write(f'{data}\n')

#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('temp.txt', 'r', encoding='UTF-8') as file:
    line_number = 0
    for line in file:
        line_number += 1
        list_line = line.split()
        words_number = len(list_line)
        print(f'Количество слов в строке {line_number} = {words_number}')
    print('Количество строк в файле: ', line_number)

#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('employers.txt', 'r', encoding='UTF-8') as file:
    poor_employers = []
    salary = 0
    count = 0
    for line in file:
        words = line.split()
        for i in words:
            if i.isdigit():
                if int(i) < 20000:
                    poor_employers.append(words[0])
                salary = salary + int(i)
        count += 1
print('Фамилии сотрудников, у которых зарплата < 20000 рублей: ', poor_employers)
print(f'Средняя зарплата сотрудников: {salary/count}')

#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dict_numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('count.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

rus_lines = []

for line in lines:
    word = line.split()
    word[0] = dict_numbers[word[0]]
    rus_line = ' '
    rus_lines.append(rus_line.join(word) + '\n')
    #rus_lines.append(' '.join(word) + '\n')

with open('count_rus.txt', 'w', encoding='UTF-8') as file:
    file.writelines(rus_lines)

#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('numbers.txt', 'w', encoding='UTF=8') as file:
    for i in range(10):
        file.write(str(randint(1, 100)) + ' ' if i != 9 else str(randint(1, 100)))

with open('numbers.txt', 'r', encoding='UTF=8') as file:
    line = file.read()
    print("Случайные числа в файле: ", line)
    summ = 0
    for i in line.split():
        summ = summ + int(i)
    print('Сумма чисел:', summ)

#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#Примеры строк файла:
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —

#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

studies_dict = {}

with open('stidues.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    for line in lines:
        words = line.split()
        summ = 0
        for word in words:
            if '(' in word:
                number = word.split('(')[0]
                summ = summ + int(number)
        studies_dict.update({line.split(':')[0]: summ})
print(studies_dict)

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