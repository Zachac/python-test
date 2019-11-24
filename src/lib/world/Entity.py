
import pprint

class Entity:
    
    def __init__(self):
        from lib.World import world
        self._location = None
        self.wheight = None
        self.name = None
        self.setLocation((0,0))
        self.id = world().nextId()

    def setLocation(self, value):
        from lib.World import world
        world().locations.get(self._location, [self]).remove(self)
        self._location = value
        world().locations.setdefault(self._location, []).append(self)

    def getLocation(self):
        return self._location

    def getCoords(self):
        if type(self._location) == tuple and len(self._location) == 2:
            return self._location
        else:
            return (None, None)

    def __repr__(self):
        lines = [f"{{ class: {self.__class__.__name__}"]
        for key, val in vars(self).items():
            lines += f"{key}: {val}".split('\n')
        return ', '.join(lines) + " }"
