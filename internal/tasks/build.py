from internal.buildings import Building_types
from internal.enums import Shield_types

class Build:
    def __init__(self):
        self.name = "build"
        self.description = (
            "Used to build new buildings if you have enough resources.\n"
            "Usage: build <Building Type>"
        )

    def run(self, args, cache):
        if not args:
            raise ValueError("Building type is required")

        if len(args) > 1:
            raise Exception("Too many arguments. Please provide only one building type.")

        building_type_input = args[0].upper()

        try:
            building_enum = Building_types[building_type_input]
        except KeyError:
            raise ValueError(f"No such building: {building_type_input}")

        print("Available shield types:")
        for shield in Shield_types:
            print(f"- {shield.name}")

        shield_input = input("Select which shield type: ").strip().upper()
        try:
            shield_enum = Shield_types[shield_input]
        except KeyError:
            raise ValueError(f"No such shield: {shield_input}")

        name = input("Enter a name for your building: ").strip()
        if not name:
            raise ValueError("Building name cannot be empty.")

        building = building_enum.create(name, 55, 55, shield_enum)
        cache.buildings.add(building)
        print(f"Successfully built '{name}' with shield '{shield_enum.name}'.")
