import json
from flask import Flask, jsonify, request, redirect, url_for, render_template
from cargoJSONS import usuarios, peliculas
from funciones import home, devolver_usuarios, devolver_usuario_por_id, devolver_peliculas, check_login

app = Flask(__name__)


# Endpoint de pagina principal
@app.route("/")
<<<<<<< HEAD
def home():
    peliculas_list = []
    peliculas_list = peliculas()
    for pelicula in peliculas["peliculas"]:
        peliculas_list.append(pelicula)
    return render_template("home.html", peliculas_list=peliculas_list)
=======
def ruta_home():
    return home()

>>>>>>> b470a263a6fd8b815c90f841e4d4d01751517fa3

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


<<<<<<< HEAD
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
=======
# Endpoint de LOGIN - Ruta que va a funciones.py, si el metodo es get nos devuelve un html de login, si el metodo es post nos
# checkea que los datos son v'alidos y a partir de eso nos redirecciona a bad-login o welcome Endpoint
@app.route("/login", methods=["GET", "POST"])
def login():
    return check_login()
>>>>>>> b470a263a6fd8b815c90f841e4d4d01751517fa3


@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
