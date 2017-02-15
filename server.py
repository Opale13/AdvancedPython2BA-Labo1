import json
import os.path

import cherrypy
from cherrypy.lib.static import serve_file
import jinja2

import jinja2plugin
import jinja2tool

import utils

class Labo1():

    @cherrypy.expose
    def index(self):
        pass

    @cherrypy.expose
    def fact(self):
        pass

    @cherrypy.expose
    def factorial(self, number):
        x = utils.fact(number)

        return {"number": number, "fact": x}


if __name__ == '__main__':
    ENV = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    jinja2plugin.Jinja2TemplatePlugin(cherrypy.engine, env=ENV).subscribe()
    cherrypy.tools.template = jinja2tool.Jinja2Tool()

    cherrypy.quickstart(Labo1(),'','serveur.conf')
