from internal.buildings.buildings import *
from internal.cache import Cache
from dataclasses import dataclass
from internal.backgroundtask.resourcecontrol import metaldeplete, waterdeplete, oxygendeplete, Burnrates


import threading

cache = Cache()
resource_lock = threading.Lock()



def mindeple():
    while True:
        metaldeplete(cache, resource_lock)
        waterdeplete(cache, resource_lock)
        oxygendeplete(cache, resource_lock)


def main():
    global Burnrates
    t = threading.Thread(target=mindeple, daemon=True)
    t.start()
    
    while True:
        print(cache.resources.getresources())
        try:
            Burnrates.metal = int(input("Enter a number:"))
        except ValueError:
            print("That's not a valid Number.")

main()
