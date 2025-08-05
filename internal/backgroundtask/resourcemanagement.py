import time

from internal.enums import Resource_types, Burnrates

class ResourceManager:
    def __init__(self):
        for res in Resource_types:
            setattr(self, res.name.lower(), 10000)

    def __repr__(self):
        return str({key: value for key, value in self.__dict__.items()})
    
    def getresources(self):
        return self.__dict__

    def resourcedeplete(self, resource_lock):
        with resource_lock:
            for res in Resource_types:
                name = res.name.lower()
                currentresource = getattr(self, name)
                burnrate = getattr(Burnrates, name)
                if currentresource >= burnrate:
                    setattr(self, name, currentresource - burnrate)
        time.sleep(0.01)

