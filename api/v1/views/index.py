#!/usr/bin/python3
""" returns index view """


from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    """ returns status in json format """
    return jsonify({"status": "OK"})
