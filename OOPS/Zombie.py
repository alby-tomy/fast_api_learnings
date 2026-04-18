from Enemy import Enemy

class Zombie(Enemy):
    def __init__(self,  health_points, attack_damage):
        super().__init__(type_of_enemy="Zombie", health_points=health_points, attack_damage=attack_damage) #overriding super class constructor

    def talk(self):
        print(f"Grrr, I am a Zombie and I will eat your brains!")
    
    def spread_disease(self):
        print(f"The Zombie is spreading a deadly disease!")