#!/usr/bin/env python3

"""
Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self):
        self.__name = 'Arduino nano V3'
        self.__price = 3400

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'name = {self.get_name()}, price = {self.get_price()}p'


print('with old price (child class ):')
item_info = ItemDiscountReport()
print(item_info.get_parent_data())

print('with old price (parent class ):')
item = ItemDiscount()
print(item.get_price())

print('with new price (child class ):')
item_info.set_price(2400)
print(item_info.get_parent_data())

print('with new price (parent class ):')
item.set_price(2400)
print(item.get_price())
