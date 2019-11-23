
import cherrypy

class SimpleHttpError(cherrypy.HTTPError):
    def get_error_page(self, *args, **kwargs):
        cherrypy.response.status = self.code
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        if self._message == None:
            return b''
        else:
            return bytes(self._message, 'utf-8')