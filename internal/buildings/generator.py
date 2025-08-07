from internal.buildings.base import Base
from internal.enums import Generator_types

class Generator(Base):
    def __init__(self, name, health, defense, generator_type:Generator_types):
        super().__init__(name, health, defense)
        self.type = generator_type
