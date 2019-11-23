#!/usr/bin/python3.7
import cherrypy

from lib.world.Entity import Entity
from lib.http.CherryRequestHandler import CherryRequestHandler


if __name__ == "__main__":
    Entity()

    try:
        print("starting server")
        cherrypy.quickstart(CherryRequestHandler())
    except KeyboardInterrupt:
        pass
