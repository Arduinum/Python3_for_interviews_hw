#!/usr/bin/env python3

"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет
отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.
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


class ItemDiscountReportName(ItemDiscount):
    def get_info(self):
        return f'name = {self.get_name()}'


class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        return f'price = {self.get_price()}p'


way1 = ItemDiscountReportName().get_info()
print(way1)
way1 = ItemDiscountReportPrice().get_info()
print(way1)

way2 = getattr(ItemDiscountReportName(), 'get_info')()
print(way2)
way2 = getattr(ItemDiscountReportPrice(), 'get_info')()
print(way2)

way3 = ItemDiscountReportName.__dict__['get_info'].__get__(ItemDiscountReportName())()
print(way3)
way3 = ItemDiscountReportPrice.__dict__['get_info'].__get__(ItemDiscountReportPrice())()
print(way3)
