import pickle
import json

my_favourite_group = dict(name='Г.М.О.', tracks='[‘Последний месяц осени’, ‘Шапито’]', age=[20, 89],
                          Albums='[{‘name’: ‘Делать панк-рок’,‘year’: 2016}, {‘name’: ‘Шапито’,‘year’: 2014}]')

print(f' просто вывод в терминал---->{my_favourite_group} ')
print(type(my_favourite_group))
j_group = json.dumps(my_favourite_group)
print(f'json.dumps перевод О в текст типа строка ->{j_group}')
print(type(j_group))
p_group = pickle.dumps(my_favourite_group)
print(f'pickle.dumps переводит О в байты--> {my_favourite_group}')
print(type(p_group))
with open('group.txt', 'wb') as f:
    pickle.dump(my_favourite_group, f)

print('my_favourite_group записан')
# //////////////////
with open('group.json', 'w', encoding='utf-8') as f:  # почему не wb?
    json.dump(my_favourite_group, f)
print('my_favourite_group записан в .json')
