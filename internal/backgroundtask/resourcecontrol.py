import threading
from dataclasses import dataclass
import time

@dataclass
class Burnrates:
    water = 0
    metal = 0
    oxygen = 0


def metaldeplete(cache, resource_lock):
    with resource_lock:
        if cache.resources.metal >= Burnrates.metal:
            cache.resources.metal -= Burnrates.metal
    time.sleep(0.01)


def waterdeplete(cache, resource_lock):
    with resource_lock:
        if cache.resources.water >= Burnrates.water:
            cache.resources.water -= Burnrates.water
    time.sleep(0.01)

def oxygendeplete(cache, resource_lock):
    with resource_lock:
        if cache.resources.oxygen >= Burnrates.oxygen:
            cache.resources.oxygen -= Burnrates.oxygen
    time.sleep(0.01)
