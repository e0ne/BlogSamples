import datetime

import tornado.web


class NoCacheStaticHandler(tornado.web.StaticFileHandler):
    """ Request static file handlers for development and debug only.
    It disables any caching for static file.
    """
    def set_extra_headers(self, path):
        self.set_header('Cache-Control', 'no-cache, must-revalidate')
        self.set_header('Expires', '0')
        now = datetime.datetime.now()
        expiration = datetime.datetime(now.year-1, now.month, now.day)
        self.set_header('Last-Modified', expiration)
 
