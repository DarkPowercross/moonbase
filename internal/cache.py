from internal.backgroundtask import ResourceManager
from internal.backgroundtask import BuildingManagement

class Cache:
    def __init__(self):
        self.buildings = BuildingManagement()
        self.resources = ResourceManager()

