from Enemy import Enemy
import random
class Zombie(Enemy):
    def __init__(self,  health_points, attack_damage):
        super().__init__(type_of_enemy="Zombie", health_points=health_points, attack_damage=attack_damage) #overriding super class constructor

    def talk(self):
        print(f"Grrr, I am a Zombie and I will eat your brains!")
    
    def spread_disease(self):
        print(f"The Zombie is spreading a deadly disease!")

    def special_attack(self):
        did_speacial_attack_work = random.random() < 0.50 # 50% chance of success
        if did_speacial_attack_work:
            self.health_points += 2
            print("Zombie regererated 2 health points!")