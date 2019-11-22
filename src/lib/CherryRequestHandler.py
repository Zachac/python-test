import cherrypy
import pprint
from lib.World import world
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
