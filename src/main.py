#!/usr/bin/python3.7
import cherrypy

from lib.world.Entity import Entity
from lib.CherryRequestHandler import CherryRequestHandler


if __name__ == "__main__":
    try:
        print("starting server")
        cherrypy.quickstart(CherryRequestHandler())
    except KeyboardInterrupt:
        pass
