
import pprint
from http.server import BaseHTTPRequestHandler
from lib.World import World
from lib.world.Map import Map

class HttpRequestHandler(BaseHTTPRequestHandler):

    defaultHandler = lambda self: "200! OK"
    handlers = {}
    
    def do_GET(self):
        handler = HttpRequestHandler.handlers.get(self.path, HttpRequestHandler.defaultHandler);
        response = handler(self);

        if response == None:
            self.send_response(404)
        else:
            self.send_response(200)

        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(pprint.pformat(handler(self)), 'utf-8'))


HttpRequestHandler.handlers["/world"] = lambda self: World.locations
HttpRequestHandler.handlers["/entity"] = lambda self: None
HttpRequestHandler.handlers["/map"] = lambda self: Map.getMap(0,0)
