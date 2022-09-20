#!/usr/bin/python3
"""
index.py file returns status and stats of API
"""

from api.v1.views import app_views
from flask import jsonify
# import json
from models import storage


@app_views.route('/status')
def status():
    """
    Returns status as a flask response
    """
    python_dict = {"status": "OK"}
    # The jsonify() returns a flask.Response() object that already has the
    # appropriate content-type header ‘application/json’ for use with json
    # responses. Whereas, the json.dumps() method will just return an encoded
    # string, which would require manually adding the MIME type header.
    # json_string = json.dumps(python_dict)
    flask_response = jsonify(python_dict)
    return flask_response


@app_views.route('/stats')
def stats():
    """
    Returns the number of all objects by type class as a flask response
    """
    python_dict = {"amenities": storage.count("Amenity"), "cities": storage.
                   count("City"), "places": storage.count("Place"), "reviews":
                   storage.count("Review"), "states": storage.count("State"),
                   "users": storage.count("User")}
    flask_response = jsonify(python_dict)
    return flask_response
