#!/usr/bin/python3
"""
Return status of API
"""

from api.v1.views import app_views
from flask import jsonify
# import json


@app_views.route('/status')
def status():
    python_dict = {"status": "OK"}
    # The jsonify() returns a flask.Response() object that already has the
    # appropriate content-type header ‘application/json’ for use with json
    # responses. Whereas, the json.dumps() method will just return an encoded
    # string, which would require manually adding the MIME type header.
    # json_string = json.dumps(python_dict)
    flask_response = jsonify(python_dict)
    return flask_response
