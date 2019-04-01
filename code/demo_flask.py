# ===============================================================
# Author: Rodolfo Ferro
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro, for
# his workshop in HackSureste 2019 at Universidad Modelo
# in Mérida. Any explicit usage of this script or its
# contents is granted according to the license provided and
# its conditions.
# ===============================================================

# -*- coding: utf-8 -*-

from flask import Flask
from reddit_news_reader import reddit_headlines

app = Flask(__name__)


@app.route('/')
def url_principal():
    return "<h1>Hello world!</h1>"


@app.route('/pepe/')
def url_pepe():
    return "Hola soy pepe."


@app.route('/reddit/<int:n>')
def url_number(n):
    titles = reddit_headlines('artificial', n)
    return "<h1>Títulos:</h1><p>{}</p>".format(titles)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
