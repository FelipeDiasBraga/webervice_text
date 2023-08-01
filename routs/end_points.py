import json

from Database.user_sql import get_list_clientes as clientes
from Database.user_sql import get_estoque as estoque
from Database.user_sql import save_user as user
from Database.user_sql import dados_json_bd as dados_json
from flask import Blueprint, jsonify, request

user_routes = Blueprint("/user", __name__, url_prefix="/user")


@user_routes.route("/get_user_json/", methods=['POST', 'GET'])
def get_user_json():
    # um endpoint que recebe os metodo de argumentos como json
    # usado para quando preciso resceber dados em listas ou json
    args = request.get_json()

    nome = args.get("nome", str)
    email = args.get("email", str)
    telefone = args.get("telefone", str)
    endereco = args.get("endereco", str)

    usuario = user(nome, email, telefone, endereco)

    print(f"nome:{nome}", f"email:{email}", f"telefone:{telefone}", f"endereço:{endereco}")

    response = jsonify(usuario)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response, 200


@user_routes.route("/get_user/", methods=['GET'])
def get_user():
    # um endpoint que recebe os dados com metodo de argumentos normal do tipo args

    nome = request.args.get("nome", str)
    email = request.args.get("email", str)
    telefone = request.args.get("telefone", str)
    endereco = request.args.get("endereco", str)

    usuario = user(nome, email, telefone, endereco)

    print(f"nome:{nome}", f"email:{email}", f"telefone:{telefone}", f"endereço:{endereco}")

    response = jsonify(usuario)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200


@user_routes.route("/get_clientes/", methods=['GET'])
def get_clientes():
    rows_clientes = clientes()
    response = jsonify(rows_clientes)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200


@user_routes.route("/get_estoque/", methods=["GET"])
def get_estoque():
    produtos = request.args.get("produtos", False, int)
    id = request.args.get("id", None, int)
    if produtos and id:
        poduct = estoque(produtos, id)

        response = jsonify(poduct)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    else:
        select = "dados inesitentes"
        response = jsonify(select)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200


@user_routes.route("/get_dados_json_direto_do_banco/", methods=["GET"])
def get_tranformat_em_json():
    response = jsonify(dados_json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200


