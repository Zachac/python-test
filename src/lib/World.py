import itertools
import pickle

from lib.world.Users import Users

class World:
    _instance = None

    def __init__(self):
        self.locations = {}
        self._idGenerator = itertools.count(1).__next__;
        self.users = Users()

    def nextId(self):
        return self._idGenerator()

    def getEntities(self, location):
        return self.locations.get(location, [])

World._instance = World();

def world():
    return World._instance

def save():
    f = open('saves/world.pickle', 'wb')
    pickle.dump(World._instance, f)
    f.close()

def load():
    f = open('saves/world.pickle', 'rb')
    World._instance = pickle.load(f)
    f.close()
