#!/usr/bin/python3.7
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

from lib.World import World
from lib.world.Entity import Entity
from lib.HttpRequestHandler import HttpRequestHandler

def run(server_class=ThreadingHTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

Entity()
Entity().setLocation((0, 2))

try:
    print("starting server")
    run(handler_class=HttpRequestHandler)
except KeyboardInterrupt:
    pass
