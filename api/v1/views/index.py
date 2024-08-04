#!/usr/bin/python3
""" returns index view """


from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """ returns status in json format """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """ returns the number of each object by its type """
    counts = storage.count()
    return jsonify(counts)
