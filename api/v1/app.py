#!/usr/bin/python3
"""
This codebase is the entry point of the whole project
"""


import os
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


def close_storage(exception=None):
    """ closes storage before app tear down """
    storage.close()


@app.teardown_appcontext
def teardown(exception):
    """ override teardown method """
    close_storage(exception)


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
