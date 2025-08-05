from enum import Enum

from .shield import Shield
from .generator import Generator
from .storage import Storage
from .greenhouse import Greenhouse

class Building_types(Enum):
    SHIELD = Shield
    GENERATOR = Generator
    STORAGE = Storage
    GREENHOUSE = Greenhouse

    def create(self, *args, **kwargs):
        return self.value(*args, **kwargs)
