from dataclasses import make_dataclass
from enum import Enum, auto

class Resource_types(Enum):
    WATER = auto()
    METAL = auto()
    OXYGEN = auto()
    ELECTRICITY = auto()
    FOOD = auto()
    MINERALS = auto()


resource_types_fields = []

for res in Resource_types:
        name = res.name.lower()
        field_type = int
        default_value = 0
        resource_types_fields.append((name, field_type, default_value))

Burnrates = make_dataclass("Burnrates", resource_types_fields)
Growthrates = make_dataclass("Growthrates", resource_types_fields)