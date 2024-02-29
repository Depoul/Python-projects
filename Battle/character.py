from weapon import fists
from healthBar import HealthBar

class character:
    #Character constructor
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists #weapon initialized whith the fist as default weapon 

    #attack method
    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)   #setting the minimum health reachable to 0
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

#Hero class definition
class Hero(character):
    #Hero constructor
    def __init__(self,
                 name: str,
                 health: int,
                 )->None:
        super().__init__(name = name, health = health)
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")
    
    #equip weapon method definition
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    #drop weapon method
    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon



#Enemy class definition
class Enemy(character):
    #enemy constructor
    def __init__(self,
                 name: str,
                 health: int,
                 weapon,
                 ) -> None:
        super().__init__(name = name, health = health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color="red")