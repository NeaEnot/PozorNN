import os
import json

files = os.listdir('Dataset')
dictionary = {}
i = 1

for file in files:
    with open(f'Dataset\\{file}', 'r', encoding='utf-8') as file:
         for line in file:
             for ch in line:
                 if ch not in dictionary.keys():
                     print(ch)
                     dictionary[ch] = i
                     i += 1

with open('Dictionary.json', 'w') as dump:
    dump.write(json.dumps(dictionary))