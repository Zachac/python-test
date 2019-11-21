from lib.World import World

class Entity:
    
    def __init__(self):
        self.location = None
        self.setLocation((0,0))

    def setLocation(self, value):
        World.locations.get(self.location, [self]).remove(self)
        self.location = value
        World.locations.setdefault(self.location, []).append(self)

