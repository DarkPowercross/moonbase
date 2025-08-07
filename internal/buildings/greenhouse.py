from internal.buildings.base import Base

class Greenhouse(Base):
    def __init__(self, name, health, defense):
        super().__init__(name, health, defense)
