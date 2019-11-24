import bcrypt
import cherrypy
import uuid
import os

from lib.http.SimpleHttpError import SimpleHttpError

from lib.world.Entity import Entity

class Users:
    
    def __init__(self):
        self.all = {}

    def login(self, name, password):
        user = self.all.get(name, None)

        if user == None:
                raise SimpleHttpError(404, 'User does not exist')
        else:
            return user.login(password)

    def getUser(self, name):
        user = self.all.get(name, None)

        if user == None:
            print(name)
            raise SimpleHttpError(404, 'User does not exist')
        else:
            return user

    def register(self, name, password):
        user = self.all.get(name, None)

        if user == None:
            lock = Lock()
            result = self.all.setdefault(name, lock)

            # handle possible race condition
            if lock != result:
                raise SimpleHttpError(409, 'User already exists')

            self.all[name] = User(name, password)
        else:
            raise SimpleHttpError(409, 'User already exists')

class Lock:
    pass

class User(Entity):

    def __init__(self, name, password):
        Entity.__init__(self)
        self.name = name
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())
        self.sessions = []

    def login(self, password):
        if bcrypt.checkpw(password, self.password):
            return self.generateSession()
        else:
            raise SimpleHttpError(401, 'Invalid password')

    def generateSession(self):
        sessionId = str(uuid.UUID(bytes=os.urandom(16)))
        self.sessions.append(sessionId)
        return sessionId
        
    def validateSessionId(self, sessionId):
        if not sessionId in self.sessions:
            raise SimpleHttpError(401, 'Invalid sessionId')
