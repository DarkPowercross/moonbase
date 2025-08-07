
from internal.cache import Cache
from internal.enums import Burnrates, Resource_types

import time
import threading

from internal.enums.task_types import commands, completer
import readline

readline.set_completer(completer)
readline.parse_and_bind("tab: complete") 

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
            option = input("Enter a command:")
            args = option.split(" ")
            commands[args[0]].run(args[1:], cache)
        except Exception as e:
            print(e)
        except (ValueError, KeyError):
            ...

main()
