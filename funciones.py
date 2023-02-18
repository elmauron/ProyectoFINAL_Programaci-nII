import json
import uuid
from datetime import datetime
from flask import Flask, jsonify, request, redirect, url_for, render_template
from cargoJSONS import usuarios, peliculas, generos


# Funcion para mostrar peliculas en pantalla >> itera sobre la variable proveniente del archivo cargoJSONS.py
# con estructura de datos en python de peliculas y las muestra todas.
def home():
    peliculas_list = []
    peliculas_result = peliculas()
    for pelicula in peliculas_result["peliculas"]:
        peliculas_list.append(pelicula)
    return render_template("home.html", peliculas_list=peliculas_list)


# Funcion para buscar peliculas de directores especificos >> itera sobre la variable proveniente del archivo cargoJSONS.py
# con estructura de datos en python de peliculas y acorde a lo que matchee, las devuelve.
def buscar_pelicula():
    busqueda = request.form["busqueda"]
    busqueda = busqueda.upper()  # Convertir a mayúsculas
    resultados = []
    peliculas_result = peliculas()
    for pelicula in peliculas_result["peliculas"]:
        if pelicula["director"].upper() == busqueda or pelicula["titulo"].upper() == busqueda:
            resultados.append(pelicula)
    return render_template("resultados.html", busqueda=busqueda, resultados=resultados)


# Funcion para devolver la lista de usuarios con sus respectivos datos >> guarda los datos en "usuarios_result" y los imprime por consola.
def devolver_usuarios():
    usuarios_result = usuarios()
    print(type(usuarios_result))
    return (usuarios_result)


# Funcion para devolver usuarios por ID especifico >> los pasa a "usuarios_result" y tomando el ID dado, compara y devuelve el indicado.
#  De no ser así avisa con mensaje 404.
def devolver_usuario_por_id(id):
    id_int = int(id)
    usuarios_result = usuarios()
    for usuario in usuarios_result["usuarios"]:
        if usuario["id"] == id_int:
            return jsonify(usuario), 200
    return jsonify({"message": "Usuario no encontrado"}), 404


# Funcion para devolver la lista de peliculas con sus respectivos datos >> guarda los datos en "peliculas_result" y los imprime por consola.
def devolver_peliculas():

    if request.method == "GET":
        peliculas_result = peliculas()
        print(type(peliculas_result))
        return (peliculas_result)

    if request.method == "POST":
        peliculas_result = peliculas()
        return peliculas_result

    if request.method == "PUT":
        peliculas_result = peliculas()
        return peliculas_result

# Funcion para verificar datos de LOGIN >> Muestra el html y en caso de enviar
# el formulario, revisa y compara que sean correctos con un ciclo "for".
# Si los datos son correctos, redirecciona al usuario hacia ruta "/welcome".
# Si los datos son incorrectos, muestra el html bad-login para que intente nuevamente.


def check_login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":

        usuarios_result = usuarios()

        current_user = request.form.get("username")
        password = request.form.get("password")

        for usuario in usuarios_result["usuarios"]:
            if usuario['username'] == current_user and usuario['password'] == password:
                return redirect(url_for("ruta_welcome", usuario_actual=current_user))

    return render_template("bad-login.html")


# Funcion
def welcome(usuario_actual):
    peliculas_list = []
    peliculas_result = peliculas()
    for pelicula in peliculas_result["peliculas"]:
        peliculas_list.append(pelicula)
    return render_template("welcome.html", usuario_actual=usuario_actual,  peliculas_list=peliculas_list)

# Funcion para agregar comentarios >> Utiliza al usuario y el comentario que haga como parámetros y los guarda
# en la variable "comment_info" a la par con la fecha y horario del comentario.
# Se llama a la función opiniones() para obtener el contenido actual del archivo opiniones.json y se lo asigna a la variable comentarios.
# Despues se agrega el nuevo comentario a la lista de comentarios.


def cargar_comentario(usuario_actual, comment, id_int):

    print(comment)

    comment_id = str(uuid.uuid4())  # genera un ID unico para cada comment

    comment_info = {"usuario": usuario_actual, "texto": comment,
                    "hora": str(datetime.now()), "comentario_id": comment_id}

    peliculas_result = peliculas()

    for pelicula in peliculas_result["peliculas"]:
        if pelicula["id"] == id_int:
            pelicula["comentarios"].append(comment_info)

    with open("jsons/peliculas.json", "w") as file:
        json.dump(peliculas_result, file)


def peliculasCRUD(usuario_actual, id):
    print("peliculasCRUD called")
    print(request.method)
    id_int = int(id)

    if request.method == "GET":
        peliculas_result = peliculas()
        for pelicula in peliculas_result["peliculas"]:
            if pelicula["id"] == id:
                return render_template("pelicula.html", pelicula=pelicula, usuario_actual=usuario_actual)

    if request.method == "POST":
        print("llego a post")
        comment = request.form.get("comentario")
        print(comment)
        cargar_comentario(usuario_actual, comment, id_int)
        return redirect(url_for("ruta_pelicula", usuario_actual=usuario_actual, id=id))

    if request.method == "DELETE":
        peliculas_result = peliculas()
        for pelicula in peliculas_result["peliculas"]:
            if pelicula["id"] == id:
                # Elimina la pelicla de la lista
                peliculas_result["peliculas"].remove(pelicula)
                # Escribe los datos caargados
                with open("peliculas.json", "w") as f:
                    json.dump(peliculas_result, f)
                return "Pelicula borrada."
        # Si no encuentra la pelicula devuelve error 404
        return "Movie not found", 404


def editar_pelicula(usuario_actual, id):

    if request.method == "GET":
        peliculas_result = peliculas()
        for pelicula in peliculas_result["peliculas"]:
            if pelicula["id"] == id:
                return render_template("editar.html", pelicula=pelicula, usuario_actual=usuario_actual)

    if request.method == "POST":
        # Carga el archivo JSON
        with open("jsons/peliculas.json", "r") as json_file:
            data = json.load(json_file)

        # Actualiza los datos necesarios
        for pelicula in data["peliculas"]:
            if pelicula["id"] == id:
                pelicula["titulo"] = request.form.get("titulo")
                pelicula["director"] = request.form.get("director")
                pelicula["year"] = request.form.get("year")
                pelicula["sinopsis"] = request.form.get("sinopsis")
                pelicula["imagen"] = request.form.get("imagen")

        # Guarda los cambios en el archivo JSON
        with open("jsons/peliculas.json", "w") as json_file:
            json.dump(data, json_file)

        return redirect(url_for("ruta_pelicula", usuario_actual=usuario_actual, id=id))


def editar_comentario(usuario_actual, id):

    if request.method == "POST":
        # Carga el archivo JSON
        with open("jsons/peliculas.json", "r") as json_file:
            data = json.load(json_file)

        for pelicula in data["peliculas"]:
            for comentario in pelicula["comentarios"]:  # est
                if comentario["comentario_id"] == request.form.get("comentario_id"):
                    comentario["texto"] = request.form.get("comentario_texto")

        with open("jsons/peliculas.json", "w") as json_file:
            json.dump(data, json_file)

        return redirect(url_for("ruta_pelicula", usuario_actual=usuario_actual, id=id))

# Funcion para agregar peliculas


def agregar_pelicula(usuario_actual):
    if request.method == "GET":
        return render_template("agregar.html", usuario_actual=usuario_actual)

    if request.method == "POST":
        titulo = request.form.get("titulo")
        director = request.form.get("director")
        year = request.form.get("year")
        genero = request.form.get("genero")
        sinopsis = request.form.get("sinopsis")

        peliculas_result = peliculas()
        nueva_pelicula = {
            "id": len(peliculas_result["peliculas"]) + 1,
            "titulo": titulo,
            "director": director,
            "year": year,
            "genero": genero,
            "sinopsis": sinopsis,
            "imagen": "/static/img/signito.jpg",
            "comentarios": []
        }

        peliculas_result["peliculas"].append(nueva_pelicula)
        with open("jsons/peliculas.json", "w") as file:
            json.dump(peliculas_result, file)

        return redirect(url_for("ruta_welcome", usuario_actual=usuario_actual))


def devolver_directores():
    if request.method == "GET":
        peliculas_result = peliculas()
        directores = []
        for pelicula in peliculas_result["peliculas"]:
            directores.append(pelicula["director"])
        return directores


def devolver_generos():
    if request.method == "GET":
        generos_result = generos()
        generos_nombres = []
        for genero in generos_result["generos"]:
            generos_nombres.append(genero["nombre"])
        return generos_nombres


def devolver_pelicula_por_director(director):
    if request.method == "GET":
        peliculas_result = peliculas()
        titulos = []

        for pelicula in peliculas_result["peliculas"]:
            if pelicula["director"] == director:
                titulos.append(pelicula["titulo"])
        return titulos


def devolver_pelicula_con_imagen():
    if request.method == "GET":

        peliculas_result = peliculas()
        peliculas_con_imagen = []

        for pelicula in peliculas_result["peliculas"]:
            if pelicula["imagen"]:
                peliculas_con_imagen.append(pelicula["titulo"])
        return peliculas_con_imagen
