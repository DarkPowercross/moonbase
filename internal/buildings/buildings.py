from enum import Enum

building_costs = {
    "SHIELD": {
        "RADIATION":{"METAL": 500, "WATER": 100, "OXYGEN": 200, "HEALTH": 2000, "DEFENSE": 2500},
        "THERMAL":{"METAL": 500, "WATER": 100, "OXYGEN": 200, "HEALTH": 2000, "DEFENSE": 2500},
        "DEFLECTOR":{"METAL": 500, "WATER": 100, "OXYGEN": 200,"HEALTH": 2000, "DEFENSE": 2500}
        },
    "STORAGE": {
        "OXYGEN":{"METAL": 600, "WATER": 300, "OXYGEN": 200, "HEALTH": 2000, "DEFENSE": 2500},
        "METAL":{"METAL": 600, "WATER": 300, "OXYGEN": 200, "HEALTH": 2000, "DEFENSE": 2500},
        "WATER":{"METAL": 600, "WATER": 300, "OXYGEN": 200, "HEALTH": 2000, "DEFENSE": 2500},
        "FOOD":{"METAL": 600, "WATER": 300, "OXYGEN": 200, "HEALTH": 2000, "DEFENSE": 2500}
        },
    "GENERATOR": {
        "SOLAR":{"METAL": 500, "WATER": 0, "OXYGEN": 200, "HEALTH": 2000, "DEFENSE": 2500},
        "NUCLEAR":{"METAL": 500, "WATER": 0, "OXYGEN": 200, "HEALTH": 2000, "DEFENSE": 2500}
        },
    "GREENHOUSE": {"METAL": 500, "WATER": 0, "OXYGEN": 200, "HEALTH": 2000, "DEFENSE": 2500},
    "HOMEPOD": {"METAL": 500,"WATER": 0, "OXYGEN": 200, "HEALTH": 2000, "DEFENSE": 2500}
}
    
class Storage_types(Enum):
    FOOD = 0
    OXYGEN = 1
    WATER = 2
    METAL = 3

class Shield_types(Enum):
    RADIATION = 0
    THERMAL = 1
    DEFLECTOR = 2

class Building:
    def __init__(self, health, defense):
        self.health = health
        self.defense = defense

class Shield(Building):
    def __init__(self, health, defense, shield_type:Shield_types):
        super().__init__(health, defense)
        self.type = shield_type

    def __repr__(self):
        return f"<Shield(type={self.type.name}, health={self.health}, defense={self.defense})>"

class Greenhouse(Building):
    def __init__(self, health, defense):
        super().__init__(health, defense)

class Storage(Building):
    def __init__(self, health, defense, storage_type:Storage_types):
        super().__init__(health, defense)
        self.building_type = storage_type
        self.quantity = 0

class Generator(Building):
    def __init__(self, health, defense):
        super().__init__(health, defense)

class Building_types(Enum):
    SHIELD = Shield
    GENERATOR = Generator
    STORAGE = Storage
    GREENHOUSE = Greenhouse
    
    def create(self, *args, **kwargs):
        return self.value(*args, **kwargs)