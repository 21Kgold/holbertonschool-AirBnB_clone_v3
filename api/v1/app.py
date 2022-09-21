#!/usr/bin/python3
"""
Create variable app as instance of flask
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def handle_404(error):
    """
    Custom message for 404 error
    """
    return (jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def storage_close(self):
    """
    Method to handle @app.teardown_appcontext that calls storage.close()
    """

    storage.close()


if __name__ == "__main__":
    # os.getenv() method returns the value of the environment variable key
    # i.e. HBNB_API_HOST if it exists otherwise returns the default value,
    # i.e. 0.0.0.0
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=getenv('HBNB_API_PORT', '5000'), threaded=True)
