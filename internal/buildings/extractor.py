from internal.buildings.base import Base
from internal.enums import Extractor_types

class Extractor(Base):
    def __init__(self, name, health, defense, extractor_type:Extractor_types):
        super().__init__(name, health, defense)
        self.type = extractor_type
