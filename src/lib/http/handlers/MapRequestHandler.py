import cherrypy

from lib.world.Map import Map

class MapRequestHandler:
    
    @cherrypy.expose
    def map(self, x=0, y=0, size=10):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        return Map.getMap(int(x), int(y), int(size))
