import json
from datetime import datetime
from flask import Flask, jsonify, request, redirect, url_for, render_template
from cargoJSONS import usuarios, peliculas, opiniones



# Funciones para /home >>> Mostrar peliculas en pantalla + Buscar peliculas por director
def home():
    peliculas_list = []
    peliculas_result = peliculas()
    for pelicula in peliculas_result["peliculas"]:
        peliculas_list.append(pelicula)
    return render_template("home.html", peliculas_list=peliculas_list)

def buscar_pelicula():
    director = request.form["director"]
    director.upper()
    resultados = []
    peliculas_result = peliculas()
    for pelicula in peliculas_result["peliculas"]:
        if pelicula["director"] == director:
            resultados.append(pelicula)
    return render_template("resultados.html", director=director, resultados=resultados)
      
                         


def devolver_usuarios():
    usuarios_result = usuarios()
    print(type(usuarios_result))
    return (usuarios_result)


def devolver_usuario_por_id(id):
    id_int = int(id)
    usuarios_result = usuarios()
    for usuario in usuarios_result["usuarios"]:
        if usuario["id"] == id_int:
            return jsonify(usuario), 200
    return jsonify({"message": "Usuario no encontrado"}), 404

# Funciones para /home >>> Mostrar peliculas en pantalla + Buscar peliculas por director
def devolver_peliculas():
    peliculas_result = peliculas()
    print(type(peliculas_result))
    return (peliculas_result)






def check_login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":

        usuarios_result = usuarios()

        username = request.form.get("username")
        password = request.form.get("password")

        for usuario in usuarios_result["usuarios"]:
            if usuario['username'] == username and usuario['password'] == password:
                return redirect(url_for("welcome", username=username))

    return render_template("bad-login.html")


def agregar_comentario(usuario, comentario):

    comment_info = {"username": usuario, "text": comentario,
                    "timestamp": str(datetime.now())}
    comentarios = []
    try:
        with open("jsons/opiniones.json", "r") as file:
            comentarios = json.load(file)
    except:
        pass

    comentarios["comentarios"].append(comment_info)

    with open("jsons/opiniones.json", "w") as file:
        json.dump(comentarios, file)
