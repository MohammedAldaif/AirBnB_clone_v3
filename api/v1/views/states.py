#!/usr/bin/python3
""" objects that handle all default RestFul API actions for States """

from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """
    Retrieves the list of all State objects
    """
    all_states = storage.all(State).values()
    list_states = [state.to_dict() for state in all_states]
    return jsonify(list_states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ Retrieves a specific State """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """
    Deletes a State Object
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """
    Creates a State
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    instance = State(**data)
    storage.new(instance)  # Add to session
    storage.save()  # Commit changes
    print(storage.all(State))
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """
    Updates a State
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(state, key, value)
    storage.save()  # Commit changes
    print(storage.all(State))
    return make_response(jsonify(state.to_dict()), 200)
