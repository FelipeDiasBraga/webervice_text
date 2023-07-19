from Database.user_sql import get_table_carros as car
from Database.user_sql import get_dados_vadildate as valid
from Database.user_sql import save_user as user
from flask import Blueprint, jsonify, request

user_routes = Blueprint("user", __name__, url_prefix="/user")


@user_routes.route("/get_usuario/", methods=['POST'])
def get_user():
    args = request.get_json()
    name = args.get("name", None)
    email = args.get("email", None)
    senha = args.get("senha", None)

    usuario = user(name, email, senha)

    response = jsonify(usuario)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200


@user_routes.route("/get_carros/", methods=['GET'])
def get_carros():
    carros = car()

    response = jsonify(carros)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

