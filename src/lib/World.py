

class World:
    locations = {}

    @staticmethod
    def nextId():
        World._id = World._id + 1
        return World._id

    @staticmethod
    def getEntities(location):
        return World.locations.get(location, [])
