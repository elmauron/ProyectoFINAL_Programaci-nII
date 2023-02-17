import json
from flask import Flask, jsonify, request, redirect, url_for, render_template
from funciones import home, devolver_usuarios, devolver_usuario_por_id, devolver_peliculas, check_login, welcome, editar_pelicula, buscar_pelicula, peliculasCRUD, editar_comentario

app = Flask(__name__)


# Endpoint de pagina principal
@app.route("/")
def ruta_home():
    return home()


@app.route("/resultados", methods=["POST"])
def ruta_resultados():
    return buscar_pelicula()


# método GET usuarios
@app.route("/usuarios")
def ruta_usuarios():
    return devolver_usuarios()


# método GET usuarios por ID
@app.route("/usuarios/<id>")
def ruta_usuario_ID():
    return devolver_usuario_por_id()


#  método GET peliculas
@app.route("/peliculas")
def ruta_peliculas():
    return devolver_peliculas()


# Endpoint de LOGIN - Ruta que va a funciones.py, si el metodo es get nos devuelve un html de login, si el metodo es post nos
# checkea que los datos son validos y a partir de eso nos redirecciona a bad-login o welcome Endpoint
@app.route("/login", methods=["GET", "POST"])
def login():
    return check_login()


# Ruta para bienvenida >> se pasan el parámetro de "usuario_actual" que es el usuario tomado desde LOGIN
@app.route("/welcome/<usuario_actual>")
def ruta_welcome(usuario_actual):
    return welcome(usuario_actual)


@app.route("/pelicula/<usuario_actual>/<int:id>", methods=["GET", "POST"])
def ruta_pelicula(usuario_actual, id):
    return peliculasCRUD(usuario_actual, id)


@app.route("/pelicula/<usuario_actual>/<int:id>/editar", methods=["GET", "POST", "PUT", "DELETE"])
def ruta_editar(usuario_actual, id):
    return editar_pelicula(usuario_actual, id)


@app.route("/comentario/<usuario_actual>/<int:id>/editar", methods=["GET", "POST", "PUT", "DELETE"])
def ruta_editar_comentario(usuario_actual, id):
    return editar_comentario(usuario_actual, id)


if __name__ == "__main__":
    app.run(debug=True)
