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
            a = int(number_a)
            b = int(number_b)
            c = int(number_c)

            x1, x2, delta = utils.roots(a, b, c)

            root1 = str(x1)
            root2 = str(x2)
            delta = str(delta)
            function = str(a) + 'x²+' + str(b) + 'x+' + str(c) + '=0'

            return {"x1": root1, "x2": root2, "delta": delta, "function": function}

        except:
            pass

    @cherrypy.expose
    def integrate(self):
        pass

    @cherrypy.expose
    def Answer_integ(self, function, lower, upper):
        try:
            a = int(lower)
            b = int(upper)

            integrate = utils.integrate(function, a, b)

            return {"function": function, "result": integrate}
        except:
            pass

if __name__ == '__main__':
    ENV = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    jinja2plugin.Jinja2TemplatePlugin(cherrypy.engine, env=ENV).subscribe()
    cherrypy.tools.template = jinja2tool.Jinja2Tool()

    cherrypy.quickstart(Labo1(),'','serveur.conf')
