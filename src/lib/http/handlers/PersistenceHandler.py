import cherrypy

from lib.World import save, load

class PersistenceHandler:
    
    @cherrypy.expose
    def save(self):
        print("Saving world...")
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        save()
        return "Success!"

    @cherrypy.expose
    def load(self):
        print("Loading world...")
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        load()
        return "Success!"
