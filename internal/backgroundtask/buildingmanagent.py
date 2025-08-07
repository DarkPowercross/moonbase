from internal.backgroundtask.resourcemanagement import Burnrates, Resource_types
from internal.enums import Shield_types
from internal.buildings import Shield, Greenhouse

class BuildingManagement:
    def __init__(self):
        self.buildings = [
            Shield("Shield 1", health=55, defense=55, shield_type=Shield_types.RADIATION), 
            Greenhouse("Greenhouse 1", 20, 60)
            ]

    def buildingresourcecosts(self):
        total_burnrates = {res.name.lower(): 0 for res in Resource_types}

        for building in self.buildings:
            values = building.resourcedepletioncost()
            for res in Resource_types:
                name = res.name.lower()
                total_burnrates[name] += values.get(name, 0)
                
        for name, value in total_burnrates.items():
            setattr(Burnrates, name, value)


    def add(self, building):
        self.buildings.append(building)

        

