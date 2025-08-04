class Cache:
    def __init__(self):
        self.buildings = []
        self.resources = ResourceManager()

class ResourceManager:
    def __init__(self):
        self.metal = 10000
        self.water = 10000
        self.oxygen = 10000

    def __repr__(self):
        return {
            "metal": self.metal,
            "water": self.water,
            "oxygen": self.oxygen,
        }
    
    def getresources(self):
        return self.metal, self.water, self.oxygen
    