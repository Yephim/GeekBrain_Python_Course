val=0
while (val<=0) or (val>10):
    print('Введите число ,больше 0, но меньше 10')
    val = int(input())
    if (val<=0) or (val>10):
        print('Неверно')
else:
    print(val**2)
