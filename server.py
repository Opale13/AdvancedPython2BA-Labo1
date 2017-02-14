import json
import os.path

import cherrypy
from cherrypy.lib.static import serve_file
import jinja2

import jinja2plugin
import jinja2tool

class Labo1():

    @cherrypy.expose
    def index(self):
        return {"message": "Hello World"}

if __name__ == '__main__':
    ENV = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    jinja2plugin.Jinja2TemplatePlugin(cherrypy.engine, env=ENV).subscribe()
    cherrypy.tools.template = jinja2tool.Jinja2Tool()

    cherrypy.quickstart(Labo1(),'','serveur.conf')
