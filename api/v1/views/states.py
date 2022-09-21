#!/usr/bin/python3
"""
View for State objects that handles all default RESTFul API actions
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_state():
    """
    Retrives all json objects of class State
    """
    objs = storage.all("State")
    list = []
    for obj in objs.values():
        list.append(obj.to_dict())
    return jsonify(list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def id_state(state_id):
    """
    Retrives a json objects of class State of state_id
    """
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    return jsonify(obj)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """
    Deletes a json objects of class State and state_id
    """
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    obj.delete()
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """
    Create a json objects of class State
    """
    obj_data = request.get_json()
    if not obj_data:
        return (jsonify({"error": "Not a JSON"}), 400)
    name = obj_data.get("name")
    if not name:
        return (jsonify({"error": "Missing name"}), 400)
    new_obj = State(**obj_data)
    new_obj.save()
    return (jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=["PUT"], strict_slashes=False)
def update_states(state_id):
    """
    Updates an object of class State
    """

    obj_data = request.get_json()
    if obj_data is None:
        return (jsonify({"error": "Not a JSON"}), 400)
    my_obj = storage.get("State", state_id)
    if my_obj is None:
        abort(404)
    not_updatable = ["id", "created_at", "updated_at"]
    for key, value in obj_data.items():
        if key not in not_updatable:
            setattr(my_obj, key, value)
    my_obj.save()
    return jsonify(my_obj.to_dict())
