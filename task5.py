#!/usr/bin/env python3

"""
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться
переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и
возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
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
    def __init__(self, discount):
        super().__init__()
        self.__discount = discount

    def __str__(self):
        return '%s' % int(self.get_price() - (self.get_price() / 100 * self.__discount))

    def get_parent_data(self):
        return f'name = {self.get_name()}, price = {self.get_price()}p'


discount_info = ItemDiscountReport(5)
print(discount_info)  # выведет цену товара с учётом скидки
