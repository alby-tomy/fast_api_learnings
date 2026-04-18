from fast_api_learnings.OOPS.Enemy import *

enemy = Enemy()
enemy.type_of_enemy = 'Orc'
enemy.health_points = 20
enemy.attack_damage = 5

print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and {enemy.attack_damage} attack damage.')