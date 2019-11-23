import cherrypy
import pprint

from lib.World import world

class DebugHandler:

    @cherrypy.expose
    def locations(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        return pprint.pformat(world().locations)
