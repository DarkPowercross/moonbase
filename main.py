
from internal.cache import Cache
from internal.enums import Burnrates, Resource_types

import time
import threading

cache = Cache()
resource_lock = threading.Lock()

def mindeple():
    while True:
        cache.buildings.buildingresourcecosts()
        cache.resources.resourcedeplete(resource_lock)
        time.sleep(1)


def main():
    global Burnrates
    t = threading.Thread(target=mindeple, daemon=True)
    t.start()
    
    while True:
        values = cache.resources.getresources()
        print("===============")
        for type in Resource_types:
            name = type.name.lower()
            burnrate = getattr(Burnrates, name)
            print(f"{name.title()}:  {values[name]} : Burnrate: {burnrate}")
        print("===============")
        try:
            option = int(input("Enter a number:"))

        except ValueError:
            ...

main()
