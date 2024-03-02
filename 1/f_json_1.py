# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json

with open('result.txt', 'r', encoding='utf-8') as f:
    data = []
    for line in f:
        data.append(line.capitalize())
    data = ''.join(data)

with open('result.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)