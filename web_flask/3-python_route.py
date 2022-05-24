#!/usr/bin/python3
"""" Write a script that starts a Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ hello function """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def task1():
    """ hello function """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def task2(text):
    """ hello function """
    sin = text.replace("_", " ")
    return ("C %s" % sin)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def task3(text='is cool'):
    """ hello function """
    sin = text.replace("_", " ")
    return ("Python %s" % sin)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
