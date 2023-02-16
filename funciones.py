import json
from datetime import datetime
from flask import Flask, jsonify, request, redirect, url_for, render_template
from cargoJSONS import usuarios, peliculas


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
    director = request.form["director"]
    director.upper()
    resultados = []
    peliculas_result = peliculas()
    for pelicula in peliculas_result["peliculas"]:
        if pelicula["director"] == director:
            resultados.append(pelicula)
    return render_template("resultados.html", director=director, resultados=resultados)


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
    peliculas_result = peliculas()
    print(type(peliculas_result))
    return (peliculas_result)


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
                return redirect(url_for("welcome", usuario_actual=current_user))

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


def cargar_comentario(usuario, comentario, id):
    print(comentario)
    comment_info = {"ususario": usuario, "texto": comentario,
                    "hora": str(datetime.now()), "pelicula_id": id}
    pelis = peliculas()

    for pelicula in pelis:
        if pelicula["id"] == id:
            pelicula["comentarios"].append(comment_info)

    with open("jsons/peliculas.json", "w") as file:
        json.dump(pelis, file)


def peliculasCRUD(usuario_actual, id):
    print("peliculasCRUD called")

    if request.method == "GET":
        peliculas_result = peliculas()
        for pelicula in peliculas_result["peliculas"]:
            if pelicula["id"] == id:
                return render_template("pelicula.html", pelicula=pelicula)

    if request.method == "POST":
        print("llego a post")
        comment = request.form.get("comment")
        cargar_comentario(usuario_actual, comment, id)
        return redirect(url_for("ruta_pelicula", usuario_actual=usuario_actual, id=id))
