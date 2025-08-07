
from internal.enums import Resource_types

class Base:
    def __init__(self, name, health, defense):
        self.name = name
        self.health = health
        self.defense = defense
        for res in Resource_types:
            setattr(self, res.name.lower(), 1)

    def resourcedepletioncost(self):
        values = {}
        for res in Resource_types:
            name = res.name.lower()
            values[name] = getattr(self, name)
        
        return values



