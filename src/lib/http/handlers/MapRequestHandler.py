import cherrypy

from lib.world.Map import Map
from lib.http.handlers.AuthenticationHandler import Authenticationhandler

class MapRequestHandler:
    
    @cherrypy.expose
    def map(self, x=None, y=None, size=10):
        player = Authenticationhandler.getPlayer()

        if player:
            (player_x, player_y) = player.getCoords()
        else:
            (player_x, player_y) = (None, None)
        
        x = x or player_x or 0
        y = y or player_y or 0

        cherrypy.response.headers['Content-Type'] = 'text/plain'
        return Map.getMap(int(x), int(y), int(size))
