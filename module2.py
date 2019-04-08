'''
2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.
'''
import random

def random_item(list):
    if len(list) == 0:
        return None
    else:
        return random.choice(list)

if __name__ == '__main__':
    print(random_item([1, 2, 3, 4]))
    print(random_item([]))
