#!/usr/bin/env python3

"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени
файла (без расширения).
"""


from os import path


def search_file_name(name):
    path_to_file = path.abspath(name)
    name_full = path_to_file.split('/')[-1]
    return name_full.split('.')[0]


name_file = search_file_name('toyota-2000gt-1024x805.jpg')
print(name_file)
