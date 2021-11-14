#!/usr/bin/env python3

"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""

from time import time, sleep


my_list = list()
my_dict = dict()


def gen_num_random(x, y):
    if x == 0:
        return 'Минимальное число не должно быть 0!'
    time_random = time() - float(str(time()).split('.')[0])
    return int(time_random * (y - x) + x)


print(gen_num_random(1, 100))
print(gen_num_random(0, 100))
print(gen_num_random(-100, -2))


for _ in range(0, 10):
    sleep(1.3)
    my_list.append(gen_num_random(1, 100))

number = 1

for _ in range(0, 8):
    sleep(1.2)
    my_dict[f'elem_<{number}>'] = gen_num_random(1, 66)
    number += 1

print(my_list)
print(my_dict)
