import pickle
import json

with open('group.txt', 'rb') as f:
    result = pickle.load(f)
    print(f'десериализовали обратно из файла из байтов to dict-->{result}')
    print(type(result))
with open('group.json', 'r', encoding='utf-8') as f:
    r_json = json.load(f)
    print(f'десериализовали обратно из файла из str to dict--> {r_json}')
    print(type(r_json))
