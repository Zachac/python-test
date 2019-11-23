import cherrypy

from lib.World import save, load

class PersistenceHandler:
    
    @cherrypy.expose
    def save(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        save()
        return "Success!"

    @cherrypy.expose
    def load(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        load()
        return "Success!"
