
'''
1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код.
Затем создайте вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.
'''
import os
import sys

def my_mkdir ():
    for i in range(1,10):
        new_path=os.path.join(os.getcwd(),f'dir_{i}')
        os.mkdir(new_path)

def my_rmdir ():
    for i in range(1,10):
        new_path=os.path.join(os.getcwd(),f'dir_{i}')
        os.rmdir(new_path)

if __name__=='__main__':
    print(os.listdir())
    my_mkdir()
    print(os.listdir())
    my_rmdir()
    print(os.listdir())
