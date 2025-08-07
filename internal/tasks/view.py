from internal.buildings import Building_types
from internal.enums import Shield_types


class View:
    def __init__(self):
        self.name = "view"
        self.description = "lists all buildings. Usage: view"

    def run(self,args, cache):
        for building in cache.buildings.buildings:
            print(building.name)