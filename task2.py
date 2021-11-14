#!/usr/bin/env python3

import os


def print_directory_contents(path):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """

    while True:
        result_list = [path, [], []]
        list_folders = []

        for el in os.listdir(path):
            if os.path.isfile(f'{path}/{el}'):
                result_list[2].append(el)
            else:
                result_list[1].append(el)

        yield tuple(result_list)

        if len(result_list[1]) == 0:
            return
        else:
            result_list[2].clear()
            for folder in result_list[1]:
                list_folders.append(folder)
            result_list[0] = f'{result_list[0]}/{list_folders.pop(0)}'
            path = result_list[0]


for i in print_directory_contents('Pictures'):
    print(i)

# моя функция работает если в каждом каталоге будет либо 1 либо 0 папок!
# пример вывода:
# ('Pictures', ['Pictures1'], ['.DS_Store', 'toyota-2000gt-1967-1024x641.jpg'])
# ('Pictures/Pictures1', ['Pictures2'], ['.DS_Store', 'toyota-2000gt-1024x805.jpg'])
# ('Pictures/Pictures1/Pictures2', [], ['.DS_Store', '02961135b3b30ffcc197f87ab28ab444d02f7fa6.jpg', 'unnamed.jpg'])
