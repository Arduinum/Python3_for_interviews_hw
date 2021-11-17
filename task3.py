#!/usr/bin/env python3

"""
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    def __init__(self):
        self.__name = 'Arduino nano V3'
        self.__price = 3400

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'name = {self.get_name()}, price = {self.get_price()}p'


item_info = ItemDiscountReport()
print(item_info.get_parent_data())
