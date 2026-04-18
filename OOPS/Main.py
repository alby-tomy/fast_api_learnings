from Enemy import Enemy
from Zombie import Zombie
from Oger import Oger

def battle(e : Enemy): #polymorphism
    e.talk()
    e.attack()



zombiee = Zombie( 100, 20)
oger = Oger(150, 30)

print(f'{zombiee.get_type_of_enemy()} has {zombiee.health_points} health points and does {zombiee.attack_damage} damage.')
print(f'{oger.get_type_of_enemy()} has {oger.health_points} health points and does {oger.attack_damage} damage.')
print()
print()
battle(zombiee) # Polymorphic call
battle(oger)   # Polymorphic call