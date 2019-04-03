print('Введите Имя:')
name = input()
print('Введите фамилию:')
surname=input()
print('Введите возраст:')
age=int(input())
print('Введите вec:')
weight=int(input())
if age<30 and weight>=50 and weight<120:
    print('{} {}, {} год, вес {} — хорошее состояние.'.format(name,surname,age,weight))
elif (age>30  and age<=40) and (weight<50 or weight>120):
    print('{} {}, {} год, вес {} — следует заняться собой.'.format(name,surname,age,weight))
elif age>40 and (weight<50 or weight>120):
    print('{} {}, {} год, вес {} — следует обратиться к врачу.'.format(name,surname,age,weight))
else:
    print('{} {}, {} год, вес {} — пора учить Python.'.format(name, surname, age, weight))