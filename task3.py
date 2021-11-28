#!/usr/bin/env python3

"""
Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""


cars_keys = ['car_1', 'car_2', 'car_3', 'car_4', 'car_5', 'car_6', 'car_7']
cars_meaning = ['BMW E28', 'BMW E30', 'BMW E32', 'BMW E34', 'BMW E36']


def make_dir(keys, meaning):
    dict_result = dict()

    for key in keys:
        dict_result.setdefault(key)

    for i, value in enumerate(meaning[:len(dict_result)]):
        dict_result.update({list(dict_result.keys())[i]: value})

    return dict_result


dict_1 = make_dir(cars_keys, cars_meaning)
print(dict_1)

cars_keys = ['car_1', 'car_2', 'car_3']

dict_2 = make_dir(cars_keys, cars_meaning)
print(dict_2)
