#!/usr/bin/python3
"""
    Create flask application instance (app)
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """
        by default no id
        if id extract information of corresponding id
    """
    states = storage.all(State)

    if id:
        states = states.get('State.{}'.format(id))

    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    """ remove the current SQLalchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
