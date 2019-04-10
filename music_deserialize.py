'''
2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json
и group.pickle, прочитать из них информацию. Получить объект — словарь из предыдущего задания.
'''

import json
import pickle

if __name__ == '__main__':

    with open('group.pickle', 'rb') as f:
        my_favourite_group = pickle.load(f)
        print(my_favourite_group)
    with open('group.json', 'r', encoding='utf-8') as f:
        my_favourite_group = json.load(f)
        print(my_favourite_group)