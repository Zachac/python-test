import cherrypy

from lib.World import world

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
