class weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int)-> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

iron_sword = weapon(name = "iron sword", 
                    weapon_type = "melee",
                    damage = 5,
                    value = 10)

short_bow = weapon(name = "short_bow",
                   weapon_type="ranged",
                   damage = 4,
                   value = 8)

fists = weapon(name = "fists",
                   weapon_type="melee",
                   damage = 2,
                   value = 8)