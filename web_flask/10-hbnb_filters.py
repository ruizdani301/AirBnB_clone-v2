#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models.state import State
from models import storage
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def task_11():
    """display a HTML page"""
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda x: x.name)
    states_city = {}
    for value in states:
        arrc = sorted(value.cities, key=lambda x: x.name)
        states_city[value] = arrc
    ameniti = list(storage.all(Amenity).values())
    ameniti = sorted(ameniti, key=lambda x: x.name)

    return render_template('10-hbnb_filters.html', states_city=states_city,
                           ameniti=ameniti)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
