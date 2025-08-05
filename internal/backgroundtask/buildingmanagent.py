from internal.backgroundtask.resourcemanagement import Burnrates, Resource_types
from internal.enums import Shield_types
from internal.buildings import Shield, Greenhouse

class BuildingManagement:
    def __init__(self):
        self.buildings = [
            Shield(55, 55, Shield_types.RADIATION),
            Greenhouse(20, 60)
            ]

    def buildingresourcecosts(self):
        for building in self.buildings:
            values = building.resourcedepletioncost()
            for res in Resource_types:
                name = res.name.lower()
                setattr(Burnrates, name, values[name])

        

