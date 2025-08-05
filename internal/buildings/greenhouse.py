from internal.buildings.base import Base

class Greenhouse(Base):
    def __init__(self, health, defense):
        super().__init__(health, defense)
