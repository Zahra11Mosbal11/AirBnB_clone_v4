#!/usr/bin/python3
""" Starts a Flask Web Application """

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, url_for, render_template
import uuid


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/100-hbnb')
def hbnb(the_id=None):
    """Custom template."""
    state_dict = storage.all('State').values()
    states = dict([state.name, state] for state in state_dict)
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           users=users,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
