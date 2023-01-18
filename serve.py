"""
Use livereload to serve the talk slides for local inspection.
"""
import livereload


# Hack to make livereload work when serving MathJax locally.
# See https://github.com/lepture/python-livereload/issues/174
#------------------------------------------------------------------------------
from pathlib import PosixPath
from urllib.parse import urlparse

# Tornado is a livereload dependency
from tornado.web import OutputTransform
import livereload.server


# Why do we do this?
# See https://github.com/GaretJax/sphinx-autobuild/issues/71#issuecomment-681854580
class _FixedLiveScriptInjector(livereload.server.LiveScriptInjector):
    def __init__(self, request):
        # NOTE: Using super() here causes an infinite cycle, due to
        #       ConfiguredTransform not declaring an __init__.
        OutputTransform.__init__(self, request)

        # Determine if this is an HTML page
        path = PosixPath(urlparse(request.uri).path)
        self.should_modify_request = path.suffix in ["", ".html"]

    def transform_first_chunk(self, status_code, headers, chunk, finishing):
        if not self.should_modify_request:
            return status_code, headers, chunk
        return super().transform_first_chunk(status_code, headers, chunk, finishing)


livereload.server.LiveScriptInjector = _FixedLiveScriptInjector
#------------------------------------------------------------------------------


server = livereload.Server()
server.watch("index.md")
server.watch("index.html")
server.watch("css")
server.watch("assets")
server.watch("images")
server.serve(root=".", port="8008", host="localhost", open_url_delay=1)
