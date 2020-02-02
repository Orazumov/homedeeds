#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def salary_count(hours:int, salary_per_hour:int, benefit:int) -> int:

    '''
    Функция расчитывает ЗП сотрудника.
    :param hours:int, salary_per_hour:int, benefit:int
    :return int
    '''

    return ((hours * salary_per_hour) + benefit)

hours, salary_per_hour, benefit = argv[1:]

salary = salary_count(int(hours), int(salary_per_hour), int(benefit))

print(salary)

#2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

list_numbers = [3, 2, 1, 7, 5, 9, 6, 0, 10]

new_list_numbers = [list_numbers[i] for i in range(1, len(list_numbers)) if list_numbers[i] > list_numbers[i-1]]

print(new_list_numbers)

#3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор.

print([number for number in range(20, 240, 1) if number % 20 == 0 or number % 21 == 0])

#4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

list_repeated = [2, 43, 6, 78, 4, 3, 2, 1, 2, 6, 15]

print(list_repeated)
#list_no_repeat = []

#for i in range(len(list_repeated)):
#    if list_repeated.count(list_repeated[i]) == 1:
#        list_no_repeat.append(list_repeated[i])
#    else:
#        continue

print([list_repeated[number] for number in range(len(list_repeated)) if list_repeated.count(list_repeated[number]) == 1])

#5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().

from functools import reduce

list_5_task = [number for number in range(100, 1001) if number % 2 == 0]
print(reduce(lambda x, y: x*y, list_5_task))

#6. Реализовать два небольших скрипта:
#а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
#б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle
a = int(input('Введите начальное число бесконечного списка: '))

for el in count(a):
    print(el)
    if el > 100:
        break

elements = input('Введите элементы, которые будут повторяться: ')
counter = 0
for rep_el in cycle(elements):
    if counter > 10000:
        break
    print(rep_el, end='')
    counter += 1

#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen(). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
#Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fibo_gen() -> int:

    '''
    Функция выдает факториал.
    :return: int
    '''

    fact = 1
    for el in range(1, 16):
        fact = fact * el
        yield fact

print(fibo_gen)

for el in fibo_gen():
    print(el)
