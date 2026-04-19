from Enemy import Enemy
from Zombie import Zombie
from Oger import Oger
from Hero import Hero
from Weapon import Weapon

def battle(e1 : Enemy, e2 : Enemy): #polymorphism
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('--- New Round ---')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()} : {e1.health_points} HP left.')
        print(f'{e2.get_type_of_enemy()} : {e2.health_points} HP left.')

        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print('--- Battle Over ---')
    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    elif e2.health_points > 0:
        print(f'{e2.get_type_of_enemy()} wins!')
    else:
        print("It's a tie!")

def hero_battle(enemy : Enemy, hero : Hero): #polymorphism

    while enemy.health_points > 0 and hero.health_points > 0:
        print('--- New Round ---')
        enemy.special_attack()
        print(f'{enemy.get_type_of_enemy()} : {enemy.health_points} HP left.')
        print(f'Hero : {hero.health_points} HP left.')

        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print('--- Battle Over ---')
    if enemy.health_points > 0:
        print(f'{enemy.get_type_of_enemy()} wins!')
    elif hero.health_points > 0:
        print(f'Hero wins!')
    else:
        print("It's a tie!")


zombiee = Zombie( 10, 1)
oger = Oger(20, 3)
hero = Hero(10, 1)
weapon = Weapon(weapon_type="Sword", attack_increase=2)
hero.weapon = weapon
hero.equip_weapon()

print(f'{zombiee.get_type_of_enemy()} has {zombiee.health_points} health points and does {zombiee.attack_damage} damage.')
print(f'{oger.get_type_of_enemy()} has {oger.health_points} health points and does {oger.attack_damage} damage.')
print()
print()
hero_battle(hero = hero, enemy = zombiee)