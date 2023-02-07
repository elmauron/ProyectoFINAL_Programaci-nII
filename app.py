import json
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Cargue los datos de los usuarios desde un archivo JSON
with open("jsons/usuarios.json") as f:
    usuarios = json.load(f)
    print(usuarios)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        for usuario in usuarios["usuarios"]:
            if usuario['username'] == username and usuario['password']  == password:
                return redirect(url_for("welcome", username=username))

        

    return render_template("login.html")

@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.html", username=username)
    


if __name__ == "__main__":
    app.run(debug=True)


    

