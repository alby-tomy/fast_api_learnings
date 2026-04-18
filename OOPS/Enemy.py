class Enemy:


    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    # def set_type_of_enemy(self, new_type_of_enemy):
    #     self.__type_of_enemy = new_type_of_enemy

    def talk(self):
        print(f"Grrr, I am {self.__type_of_enemy} and I will destroy you!")

    def walk_forwards(self):
        print(f"{self.__type_of_enemy} is walking towards you...")

    def attack(self):
        print(f"{self.__type_of_enemy} is attacking you for {self.attack_damage} damage!")