#!/usr/bin/env python3

"""
Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self):
        self.__name = 'Arduino nano V3'
        self.__price = 3400


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'name = {self.__name}, price = {self.__price}p'


try:
    item_info = ItemDiscountReport()
    print(item_info.get_parent_data())  # на этом месте произойдёт AttributeError, так как нет доступа к переменным
except AttributeError:
    print('AttributeError!')
