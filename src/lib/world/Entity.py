from lib.World import World
import itertools

class Entity:
    _generateId = itertools.count(1).__next__;
    
    def __init__(self):
        self._location = None
        self.wheight = None
        self.name = None
        self.setLocation((0,0))
        self.id = Entity._generateId()

    def setLocation(self, value):
        World.locations.get(self._location, [self]).remove(self)
        self._location = value
        World.locations.setdefault(self._location, []).append(self)

    def getLocation(self):
        return self._location

    def __repr__(self):
        result = "Entity("
        result += f"name={self.name}, "
        result += f"location={self._location}, "
        result += f"id={self.id}, "
        result += f"wheight={self.wheight}"
        result += ")"
        return result