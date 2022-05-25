#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models.state import State
from models import storage
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.route('/states/<st_id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def task_10(st_id=None):
    """display a HTML page"""
    sta = storage.all(State)
    key_id = None
    if st_id is not None:
        key_id = "State." + st_id
    return render_template('9-states.html', key_id=key_id, sta=sta)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
