import cherrypy
from lib.world.Map import Map

class CherryRequestHandler(object):
    @cherrypy.expose
    def map(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        return Map.getMap(0, 0)
