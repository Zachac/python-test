import itertools

class World:
    _instance = None

    def __init__(self):
        self.locations = {}
        self._idGenerator = itertools.count(1).__next__;

    def nextId(self):
        return self._idGenerator()

    def getEntities(self, location):
        return self.locations.get(location, [])

World._instance = World();

def world():
    return World._instance
