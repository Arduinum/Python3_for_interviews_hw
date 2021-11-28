#!/usr/bin/env python3

"""
Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего
примера (функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим
условиям: вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое
значение и вывод всех подстрок, состоящих из букв и цифр, например: example345.
"""


from random import randint
from os import path


def open_file(name):
    with open(name, 'r') as file:
        file_lines = file.readlines()
        entry = 0

        for index, line in enumerate(file_lines):
            if 'uno' in line:
                print(line, end='')
                file_lines[index] = line.replace('uno', 'arduino')
            if 'arduino' in line and entry == 0:
                print(line, end='')
                file_lines[index] = line.replace('arduino', 'mega')
                entry += 1

    with open(name, 'w') as file:
        for line in file_lines:
            file.write(line)


def make_file(name):
    if path.exists(name):
        print('Такой файл уже существует!')

    with open(name, 'w') as file:
        gen_nums = list(range(1, randint(10, 50)))
        gen_strings = [' - arduino_' + str(num) for num in gen_nums]
        gen_count_replace = randint(2, len(gen_strings)) // 2
        for count, i in enumerate(range(0, gen_count_replace)):
            gen_strings[i] = f' - uno_328p_{count + 1}'
        zipped = list(zip(gen_nums, gen_strings))

        for items in zipped:
            file.write(f'{items[0]}{items[1]}\n')

    open_file(name)


make_file('generate_list_2.txt')

# и вывод всех подстрок, состоящих из букв и цифр - не вижу смысла так как вывод уже с буквами и цифрами и так.
