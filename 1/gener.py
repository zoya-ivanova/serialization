# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import randint, choice

VOWELS = {'a', 'o', 'u', 'e', 'i', 'y'}

def gener_name():

# Генерирует случайное имя.

# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.

    length = randint(4, 7)
    min_letter = ord('a')
    max_letter = ord('z')
    name = []
    for _ in range(length):
        name.append(chr(randint(min_letter, max_letter)))
    flag = False
    for letter in name:
        if letter in VOWELS:
            flag = True
            break
    if not flag:
        i = randint(0, length - 1)
        letter = choice(list(VOWELS))
        name[i] = letter
    name = ''.join(name).capitalize()
    return name


def rec_file(lines: int, name: str):

# Записывает в файл имена.

    with open(name, 'a', encoding='utf-8') as f:
        for _ in range(lines):
            f.write(f'{gener_name()}\n')


if __name__ == '__main__':
    rec_file(15, 'names.txt')