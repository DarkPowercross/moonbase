from internal.buildings.base import Base
from internal.enums import Resource_types

class Storage(Base):
    def __init__(self,name, health, defense, storage_type: Resource_types):
        super().__init__(name, health, defense)
        self.building_type = storage_type
        self.quantity = 0