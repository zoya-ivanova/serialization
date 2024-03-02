# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

from random import random, randint

def g_num(lines: int, name: str):
    with open(name, 'a', encoding='utf-8') as f:
        for _ in range(lines):
            num_1 = randint(-1000, 1000)
            num_2 = random() * 2000 - 1000
            print(f'{num_1} | {num_2}', file=f)


if __name__ == '__main__':
    g_num(lines=10, name='output.txt')