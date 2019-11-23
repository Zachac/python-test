import cherrypy
import pprint
from lib.World import world, save, load
from lib.world.Map import Map

class CherryRequestHandler(object):
    @cherrypy.expose
    def map(self, x=0, y=0, size=10):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        return Map.getMap(int(x), int(y), int(size))

    @cherrypy.expose
    def locations(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        return pprint.pformat(world().locations)

    @cherrypy.expose
    def save(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        save()
        return "Success!"

    @cherrypy.expose
    def load(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        load()
        return "Success!"

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
