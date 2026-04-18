from Enemy import *

class Oger(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Oger", health_points=health_points, attack_damage=attack_damage) #overriding super class constructor

    def talk(self):
        print(f"Grrr, I am an Oger and I will crush you!")
    
    def smash(self):
        print(f"The Oger is smashing you with its huge fists!")