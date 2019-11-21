import cherrypy
from lib.world.Map import Map

class CherryRequestHandler(object):
    @cherrypy.expose
    def map(self, x=0, y=0, size=10):
        print(cherrypy.request.params)
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        return Map.getMap(int(x), int(y), int(size))
