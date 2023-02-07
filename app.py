import json
from flask import Flask, jsonify, request, redirect, url_for, render_template

app = Flask(__name__)

# Cargo los datos de los usuarios desde un archivo JSON
with open("jsons/usuarios.json") as f:
    usuarios = json.load(f)
    print(usuarios)


# Endpoint de pagina principal
@app.route("/")
def home():
    return "CFKLDLNA"


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


# Endpoint de LOGIN
@app.route("/login")
def index():
    return render_template("index.html")


# Funcion para verificar LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        for usuario in usuarios["usuarios"]:
            if usuario['username'] == username and usuario['password'] == password:
                return redirect(url_for("welcome", username=username))

    return render_template("login.html")


# Endpoint de logeados
@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.html", username=username)
    


if __name__ == "__main__":
    app.run(debug=True)
