import json
from flask import Flask, jsonify, request, redirect, url_for, render_template
from cargoJSONS import usuarios, peliculas
from funciones import home, devolver_usuarios, devolver_usuario_por_id, devolver_peliculas, check_login, agregar_comentario

app = Flask(__name__)


# Endpoint de pagina principal
@app.route("/")
def ruta_home():
    return home()


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
# checkea que los datos son v'alidos y a partir de eso nos redirecciona a bad-login o welcome Endpoint
@app.route("/login", methods=["GET", "POST"])
def login():
    return check_login()


@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.html", username=username)


@app.route("/add_comment", methods=["POST"])
def add_comment():
    username = request.form.get("username")
    comment = request.form.get("comment")
    agregar_comentario(username, comment)
    return redirect(url_for("welcome", username=username))


if __name__ == "__main__":
    app.run(debug=True)
