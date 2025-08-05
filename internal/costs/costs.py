from internal.enums import Resource_types, Shield_types, Generator_types
from internal.buildings import Building_types

building_costs = {
    Building_types.SHIELD: {Resource_types.METAL: 500, Resource_types.WATER: 100, Resource_types.OXYGEN: 200},
    Building_types.STORAGE: {Resource_types.METAL: 600, Resource_types.WATER: 300, Resource_types.OXYGEN: 200},
    Building_types.GENERATOR: {Resource_types.METAL: 600, Resource_types.WATER: 300, Resource_types.OXYGEN: 200},
    Building_types.GREENHOUSE: {Resource_types.METAL: 600, Resource_types.WATER: 300, Resource_types.OXYGEN: 200},
}

cost_type_modifier = {
    Shield_types.RADIATION: 1.25,
    Shield_types.THERMAL: 1.5,
    Shield_types.DEFLECTOR: 1.75,
    Generator_types.SOLAR: 1.25,
    Generator_types.NUCLEAR: 2    
}