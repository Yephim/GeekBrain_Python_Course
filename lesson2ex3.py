player = {'name': 'Йода', 'health': 100, 'damage':50}
enemy = {'name': 'Дарт Вейдер', 'health': 100, 'damage':50}
def attack(person1, person2):
    person1['health']-=person2['damage']

attack(player,enemy)
print(player)
attack(player,enemy)
print(player)
attack(enemy,player)
print(enemy)
