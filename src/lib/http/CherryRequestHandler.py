
from lib.http.handlers.MapRequestHandler import MapRequestHandler
from lib.http.handlers.AuthenticationHandler import Authenticationhandler
from lib.http.handlers.PersistenceHandler import PersistenceHandler
from lib.http.handlers.DebugHandler import DebugHandler

class CherryRequestHandler(MapRequestHandler, Authenticationhandler, PersistenceHandler, DebugHandler):
    pass
