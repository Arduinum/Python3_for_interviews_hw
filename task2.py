#!/usr/bin/env python3

"""
Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""


def get_type_num(num):
    float_parts = None

    if str(type(num)) == "<class 'int'>":
        return 'number type is int'
    elif str(type(num)) == "<class 'float'>":
        if '.' in str(num):
            float_parts = str(num).split('.')
        elif ',' in str(num):
            float_parts = str(num).split(',')

        if float_parts[0] == float_parts[1]:
            print('number type is float')
            return True
        else:
            print('number type is float')
            return False
    else:
        raise TypeError


type_num1 = get_type_num(1)
print(type_num1)

type_num2 = get_type_num(1.1)
print(type_num2)

type_num3 = get_type_num(10.1)
print(type_num3)

type_num4 = get_type_num("2")
print(type_num4)
