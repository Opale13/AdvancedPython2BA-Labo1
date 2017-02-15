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
    def Answer_fact(self, number):
        try:
            nbr = int(number)
            x = str(utils.fact(nbr))

            return {"number": number, "fact": x}

        except:
            return {"number": number, "fact": "None"}

    @cherrypy.expose
    def roots(self):
        pass

    @cherrypy.expose
    def Answer_roots(self, number_a, number_b, number_c):
        try:
            a = number_a
            b = number_b
            c = number_c

            x1, x2 = utils.roots(a, b, c)

            root1 = str(x1)
            root2 = str(x2)

            return {"x1": root1, "x2": root2}

        except:
            pass


if __name__ == '__main__':
    ENV = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    jinja2plugin.Jinja2TemplatePlugin(cherrypy.engine, env=ENV).subscribe()
    cherrypy.tools.template = jinja2tool.Jinja2Tool()

    cherrypy.quickstart(Labo1(),'','serveur.conf')
