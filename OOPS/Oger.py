from Enemy import *
import random

class Oger(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Oger", health_points=health_points, attack_damage=attack_damage) #overriding super class constructor

    def talk(self):
        print(f"Grrr, I am an Oger and I will crush you!")
    
    def smash(self):
        print(f"The Oger is smashing you with its huge fists!")

    def special_attack(self):
        did_speacial_attack_work = random.random() < 0.20 # 20% chance of success
        if did_speacial_attack_work:
            self.attack_damage += 4
            print("Oger's attack damage increased by 4 for the next attack!")