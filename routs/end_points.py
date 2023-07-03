
from Database.user_sql import get_carros as car
from flask import Blueprint, jsonify, request

user_routes = Blueprint("user", __name__, url_prefix="/user")


@user_routes.route("/get_carros/", methods=['GET'])
def get_carros():
    carros = car()

    response = jsonify(carros)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

