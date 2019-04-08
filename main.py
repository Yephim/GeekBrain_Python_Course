'''
3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций.
Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
'''
from module1 import *
from module2 import random_item

print(os.listdir())
my_mkdir()
print(os.listdir())
my_rmdir()
print(os.listdir())

print(random_item([1, 2, 3, 4]))
print(random_item([]))

