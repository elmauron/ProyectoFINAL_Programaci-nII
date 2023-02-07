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


if __name__ == '__main__':
    app.run()
