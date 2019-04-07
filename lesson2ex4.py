player = {'name': 'Йода', 'health': 100, 'damage':50,'armor':1.2}
enemy = {'name': 'Дарт Вейдер', 'health': 100, 'damage':50,'armor':2.1}
def attack(person1, person2):
    def damage_armor(damage,armor):
        return damage/armor
    person1['health']-=damage_armor(person2['damage'],person1['armor'])

attack(player,enemy)
print(player)
attack(player,enemy)
print(player)
attack(enemy,player)
print(enemy)
