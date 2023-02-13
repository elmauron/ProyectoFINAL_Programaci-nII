import json
from flask import Flask, jsonify, request, redirect, url_for, render_template
from cargoJSONS import usuarios, peliculas

app = Flask(__name__)


# Endpoint de pagina principal
@app.route("/")
def home():
    peliculas_list = []
    peliculas_list = peliculas()
    for pelicula in peliculas["peliculas"]:
        peliculas_list.append(pelicula)
    return render_template("home.html", peliculas_list=peliculas_list)

# método GET usuarios
@app.route("/usuarios")
def devolver_usuarios():
    usuarios_result = usuarios()
    print(type(usuarios_result))
    return (usuarios_result)


# método GET usuarios por ID
@app.route("/usuarios/<id>")
def devolver_usuario_por_id(id):
    id_int = int(id)
    usuarios_result = usuarios()
    for usuario in usuarios_result["usuarios"]:
        if usuario["id"] == id_int:
            return jsonify(usuario), 200
    return jsonify({"message": "Usuario no encontrado"}), 404

#  método GET peliculas


@app.route("/peliculas")
def devolver_peliculas():
    peliculas_result = peliculas()
    print(type(peliculas_result))
    return (peliculas_result)


# Endpoint de LOGIN
@app.route("/login")
def login():
    return render_template("login.html")


# Funcion para verificar LOGIN
@app.route("/login", methods=["GET", "POST"])
def check_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        for usuario in usuarios["usuarios"]:
            if usuario['username'] == username and usuario['password'] == password:
                return redirect(url_for("welcome", username=username))

    return render_template("bad-login.html")


# Endpoint de logeados
@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
