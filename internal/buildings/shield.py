from internal.buildings.base import Base
from internal.enums import Shield_types

class Shield(Base):
    def __init__(self, name,  health, defense, shield_type:Shield_types):
        super().__init__(name, health, defense)
        self.baseburnrate = 20
        self.type = shield_type

    def __repr__(self):
        return f"<Shield(type={self.type.name}, health={self.health}, defense={self.defense})>"
