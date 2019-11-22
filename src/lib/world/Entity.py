from lib.World import world

class Entity:
    
    def __init__(self):
        self._location = None
        self.wheight = None
        self.name = None
        self.setLocation((0,0))
        self.id = world().nextId()

    def setLocation(self, value):
        world().locations.get(self._location, [self]).remove(self)
        self._location = value
        world().locations.setdefault(self._location, []).append(self)

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