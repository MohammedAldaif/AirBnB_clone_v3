#!/usr/bin/python3
"""
This codebase is the entry point of the whole project
"""


import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


def close_storage(exception=None):
    """ closes storage before app tear down """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors and return a JSON response"""
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response


@app.teardown_appcontext
def teardown(exception):
    """ override teardown method """
    close_storage(exception)


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
