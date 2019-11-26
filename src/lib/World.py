import itertools
import pickle
import os.path

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
    file_name = 'saves/world.pickle'
    if os.path.isfile(file_name):
        f = open(file_name, 'rb')
        World._instance = pickle.load(f)
        f.close()
