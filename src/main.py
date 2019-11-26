#!/usr/bin/python3.7
import cherrypy

from lib.world.Entity import Entity
from lib.http.CherryRequestHandler import CherryRequestHandler


if __name__ == "__main__":
    Entity()

    try:
        handler = CherryRequestHandler()
        
        cherrypy.engine.subscribe('start', handler.load)
        cherrypy.engine.subscribe('stop', handler.save)
        
        cherrypy.tree.mount(object(), '/static/', config={ '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': '/home/zachac/git/python-test/html/',
            },
        })

        cherrypy.tree.mount(handler, '/api/')
        cherrypy.quickstart()
    except KeyboardInterrupt:
        pass
