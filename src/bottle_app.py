    # -*- coding: UTF-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Dois
Changelog
---------------

.. versionadded::     20.07

          Adiciona o gerenciador em chamadas http via bottle
   """

from bottle import default_app, route, static_file
from main import Main

@route('/')
def hello_world():
    return static_file('index.html', root='/home/pimentelufrj/dev/alpha/src/', mimetype='text/html')

@route('/oi')
def oi_mundo():
    return "Tutorial Dois - ensaiando uma nova rota"

@route('/vs')
def vs_mundo():
    return "Tutorial Dois - Versão do sistema: {}".format(Main().get_versao())

@route('/<filename:re:.*\.py>')
def py_mundo(filename):
    return static_file(filename, root='/home/pimentelufrj/dev/alpha/src', mimetype='text/python')

@route('/doc/<filename:re:.*\.html>')
def doc_mundo(filename):
    return static_file(filename, root='/home/pimentelufrj/dev/alpha/docs/build/html', mimetype='text/html')

@route('/doc/<filename:re:.*\.css>')
def css_mundo(filename):
    return static_file(filename, root='/home/pimentelufrj/dev/alpha/docs/build/html/', mimetype='text/css')

application = default_app()

