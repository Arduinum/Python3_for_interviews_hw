#!/usr/bin/env python3

"""
Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить
два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы.
Применить к спискам функцию zip(). Результат выполнения этой функции должен должен быть обработан и записан в файл
таким образом, чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать открытие файла и простой
построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.
"""


from random import randint
from os import path


def open_file(name):
    with open(name, 'r') as file:
        file_lines = file.readlines()
        for line in file_lines:
            print(line, end='')


def make_file(name):
    if path.exists(name):
        print('Такой файл уже существует!')

    with open(name, 'w') as file:
        gen_nums = list(range(1, randint(10, 50)))
        gen_strings = [' - arduino_' + str(num) for num in gen_nums]
        zipped = list(zip(gen_nums, gen_strings))

        for items in zipped:
            if items == zipped[-1]:
                file.write(f'{items[0]}{items[1]}')
            else:
                file.write(f'{items[0]}{items[1]}\n')

    open_file(name)


make_file('generate_list.txt')
