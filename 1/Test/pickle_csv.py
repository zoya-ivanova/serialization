# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import os


dict_list = [{1: 3}, {32: 'fds'}, {4: 5343}]
with open('dict_list.pickle', 'wb') as f:
    pickle.dump(dict_list, f)
with open('dict_list.pickle', 'rb') as f:
    data = pickle.load(f)
with open('dict_list.csv', 'w', encoding='utf-8') as f:
    for my_dict in dict_list:
        for key, value in my_dict.items():
            print(f'{key}, {value}', file=f)