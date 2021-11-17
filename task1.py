#!/usr/bin/env python3

"""
Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. Первый и второй множитель должны задаваться в
виде аргументов функции. Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку. Полученная строка
выводится в главной функции. Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""


def form_str_mul(num1, num2):
    form_str = lambda x, y: x + y

    def get_table_mul_list(a, b):
        list_mul = []
        result_str = ''
        count_num = 1

        for num in range(0, b):
            if num == b:
                list_mul.append(f'\t{a}\t*\t{count_num}\t=\t{a * count_num}\t')
            else:
                list_mul.append(f'\t{a}\t*\t{count_num}\t=\t{a * count_num}\t\n')
            count_num += 1

        list_mul = list_mul[::-1]

        for line in list_mul:
            result_str = form_str(line, result_str)

        return result_str

    print(get_table_mul_list(num1, num2))


form_str_mul(2, 10)
print('--------------------------')
form_str_mul(5, 8)
print('--------------------------')
form_str_mul(7, 1)
