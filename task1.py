#!/usr/bin/env python3

"""
Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса.
"""


class ItemDiscount:
    def __init__(self):
        self.name = 'Arduino nano V3'
        self.price = 3400


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'name = {self.name}, price = {self.price}p'


item_info = ItemDiscountReport()
print(item_info.get_parent_data())
