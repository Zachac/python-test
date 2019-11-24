import cherrypy

from lib.World import world
from lib.http.SimpleHttpError import SimpleHttpError

class Authenticationhandler:
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def login(self):
        data = cherrypy.request.json
        username = data['username']
        password = data['password']
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        sessionId = world().users.login(username, password)
        cherrypy.response.cookie['session'] = sessionId
        cherrypy.response.cookie['username'] = username
        return b''

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def register(self):
        data = cherrypy.request.json
        username = data['username']
        password = data['password']
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        world().users.register(username, password)
        return "Success!"

    @staticmethod
    def getPlayer(required=False):
        player = None
        username = cherrypy.request.cookie.get('username', None)
        if username != None:
            sessionId = cherrypy.request.cookie.get('session', None)
            if sessionId != None:
                player = world().users.getUser(username.value)
                player.validateSessionId(sessionId.value)

        if required and player == None:
            raise SimpleHttpError(400, 'Valid player not supplied')
        else:
            return player
