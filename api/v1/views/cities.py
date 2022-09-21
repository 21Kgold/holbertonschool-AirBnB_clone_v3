#!/usr/bin/python3
"""
View for City objects that handles all default RESTFul API actions
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def all_state_cities(state_id):
    """
    Retrives all json objects of class City from a defined State
    """
    objs = storage.get(State, state_id)
    if objs is None:
        abort(404)
    list = []
    for obj in objs.cities:
        list.append(obj.to_dict())
    return jsonify(list)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def id_city(city_id):
    """
    Retrives a json object from city_id
    """
    obj = storage.get(City, city_id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """
    Deletes a json objects of class City and city_id
    """
    obj = storage.get(City, city_id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_state_city(state_id):
    """
    Create a json objects of class City
    """
    my_state = storage.get(State, state_id)
    if my_state is None:
        abort(404)
    obj_data = request.get_json()
    if not obj_data:
        abort(400, 'Not a JSON')
    name = obj_data.get("name")
    if not name:
        abort(400, 'Missing name')
    obj_data['state_id'] = my_state.id
    new_obj = City(**obj_data)
    new_obj.save()
    return (jsonify(new_obj.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=["PUT"], strict_slashes=False)
def update_city(city_id):
    """
    Updates an object of class City
    """
    obj_data = request.get_json()
    if obj_data is None:
        abort(400, 'Not a JSON')
    my_obj = storage.get(City, city_id)
    if my_obj is None:
        abort(404)
    not_updatable = ["id", "state_id", "created_at", "updated_at"]
    for key, value in obj_data.items():
        if key not in not_updatable:
            setattr(my_obj, key, value)
    my_obj.save()
    return (jsonify(my_obj.to_dict()), 200)
