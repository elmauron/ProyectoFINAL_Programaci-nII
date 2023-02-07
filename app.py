import json
from flask import Flask, jsonify, Response, request
from http import HTTPStatus
app = Flask(__name__)

with open("jsons/usuarios.json", encoding='utf-8') as usuarios_json:
    usuarios = json.load(usuarios_json)


@app.route("/")
def home():
    return "Hello, Flask! ^_^ "


# endpoints para controlar usuarios


# método GET usuarios
@app.route("/usuarios")
def devolver_usuarios():
    print(type(usuarios))
    return jsonify(usuarios)

# método GET usuarios por ID


@app.route("/usuarios/<id>")
def devolver_usuario_por_id(id):
    id_int = int(id)
    for usuario in usuarios["usuarios"]:
        if usuario["id"] == id_int:
            return usuario, 200
    return {"message": "Usuario no encontrado"}, 404


if __name__ == '__main__':
    app.run()
