# -*- coding: UTF-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Dois
Changelog
---------------

.. versionadded::     20.07

          Adiciona o gerenciador em chamadas http via bottle
   """

from bottle import default_app, route
from main import Main

@route('/')
def hello_world():
    return "Tutorial Dois - aprendendo Git e Bottle"

@route('/oi')
def oi_mundo():
    return "Tutorial Dois - ensaiando uma nova rota"

application = default_app()


