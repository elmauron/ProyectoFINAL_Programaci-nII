import json
from flask import Flask, jsonify, request, redirect, url_for, render_template
from funciones import home, devolver_usuarios, devolver_usuario_por_id, devolver_peliculas, check_login, welcome, devolver_pelicula_con_imagen, editar_pelicula, buscar_pelicula, devolver_pelicula_por_director, devolver_generos, peliculasCRUD, devolver_directores, editar_comentario, agregar_pelicula

app = Flask(__name__)


# Endpoint de pagina principal
@app.route("/")
def ruta_home():
    page = request.args.get('p', 1, type=int)
    print(f"pagina:{page}")
    return home(p=page)


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
@app.route("/peliculas", methods=["GET", "POST", "PUT", "DELETE"])
def ruta_peliculas():
    return devolver_peliculas()


@app.route("/directores", methods=["GET"])
def ruta_directores():
    return devolver_directores()


@app.route("/generos", methods=["GET"])
def ruta_generos():
    return devolver_generos()


@app.route("/pelicula/<director>", methods=["GET"])
def ruta_pelicula_por_director(director):
    return devolver_pelicula_por_director(director)


@app.route("/pelicula/con_imagen", methods=["GET"])
def ruta_pelicula_con_imagen():
    return devolver_pelicula_con_imagen()

# Endpoint de LOGIN - Ruta que va a funciones.py, si el metodo es get nos devuelve un html de login, si el metodo es post nos
# checkea que los datos son validos y a partir de eso nos redirecciona a bad-login o welcome Endpoint


@app.route("/login", methods=["GET", "POST"])
def login():
    return check_login()


# Ruta para bienvenida >> se pasan el parámetro de "usuario_actual" que es el usuario tomado desde LOGIN
@app.route("/welcome/<usuario_actual>")
def ruta_welcome(usuario_actual):
    p = request.args.get('p', 1, type=int)
    print(f"pagina:{p}")
    return welcome(usuario_actual, p)

# Ruta para determinada pelicula


@app.route("/pelicula/<usuario_actual>/<int:id>", methods=["GET", "POST", "DELETE"])
def ruta_pelicula(usuario_actual, id):
    return peliculasCRUD(usuario_actual, id)

# Ruta para agregar peliculas


@app.route("/welcome/<usuario_actual>/agregar", methods=["GET", "POST"])
def ruta_agregar(usuario_actual):
    return agregar_pelicula(usuario_actual)

# Ruta para editar peliculas


@app.route("/pelicula/<usuario_actual>/<int:id>/editar", methods=["GET", "POST", "PUT", "DELETE"])
def ruta_editar(usuario_actual, id):
    return editar_pelicula(usuario_actual, id)

# Ruta para editar los comentarios de las peliculas


@app.route("/comentario/<usuario_actual>/<int:id>/editar", methods=["GET", "POST", "PUT", "DELETE"])
def ruta_editar_comentario(usuario_actual, id):
    return editar_comentario(usuario_actual, id)


if __name__ == "__main__":
    app.run(debug=True)
