# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle


with open('dict_list.csv', 'r', encoding='utf-8') as f:
    data = []
    for line in f:
        key, value = line.strip().split(',')
        data.append({key: value})
print(pickle.dumps(data))