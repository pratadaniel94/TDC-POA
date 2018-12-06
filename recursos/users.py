from flask import Blueprint, jsonify, request
from modulos.mongodb import *

def validar_json(data):
    for value in data.values():
        if not value:
            return False
    else:
        return True
            
db = connect_mongodb()


usuarios = Blueprint('usuarios', __name__)

@usuarios.route("/usuarios", methods=["GET"])
def all_users():
    return jsonify(list(db.usuarios.find()))


@usuarios.route("/usuario/<int:num>", methods=["GET"] )
def one_user(num):
    return jsonify(db.usuarios.find_one({"_id":num}))

@usuarios.route("/usuario/<int:num>", methods=["POST"])
def insert_user(num):
    data = request.get_json()
    status = validar_json(data)
    if data and status:
        # Cadastrar no mongodb
        return jsonify({"status": status})
    else:
        return jsonify({ "status": False})


@usuarios.route("/usuario/<int:num>", methods=["PUT"])
def update_user(num):
    data = request.get_json()
    status = validar_json(data)
    if data and status:
        # atualizar no mongodb
        return jsonify({"status": status})
    else:
        return jsonify({ "status": False})

@usuarios.route("/usuario/<int:num>", methods=["DELETE"])
def delete_user(num):
    return jsonify({"status":True})
