
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
