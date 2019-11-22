#!/usr/bin/python3.7
import cherrypy

from lib.world.Entity import Entity
from lib.CherryRequestHandler import CherryRequestHandler


if __name__ == "__main__":
    Entity()
    Entity().setLocation((0, 2))

    try:
        print("starting server")
        cherrypy.quickstart(CherryRequestHandler())
    except KeyboardInterrupt:
        pass
