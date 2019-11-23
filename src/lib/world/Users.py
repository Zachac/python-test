import bcrypt
import cherrypy

from lib.world.Entity import Entity

class Users:
    
    def __init__(self):
        self.all = {}

    def login(self, name, password):
        user = self.all.get(name, None)

        if user == None:
            raise cherrypy.HTTPError(404)
        else:
            return user.login(password)

    def register(self, name, password):
        user = self.all.get(name, None)

        if user == None:
            lock = Lock()
            result = self.all.setdefault(name, lock)

            # handle possible race condition
            if lock != result:
                raise cherrypy.HTTPError(409)

            self.all[name] = User(name, password)
        else:
            raise cherrypy.HTTPError(409)

class Lock:
    pass

class User(Entity):

    def __init__(self, name, password):
        self.name = name
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())

    def login(self, password):
        if bcrypt.checkpw(password, self.password):
            return self
        else:
            raise cherrypy.HTTPError(401)
