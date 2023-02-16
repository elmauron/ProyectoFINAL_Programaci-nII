# Archivo secundario para traer los datos de los JSON y meterlos en diccionarios
import json
from flask import Flask, jsonify

# Cargo los datos de los usuarios desde un archivo JSON

# Las funciones leen el contenido de los archivos ".json" en formato JSON
# y los cargan en un variables llamadas usuarios/peliculas/etc, que son estructuras de datos en Python (listas o diccionarios).
# Luego, las funciones devuelven estas variables.


def usuarios():
    with open("jsons/usuarios.json") as f:
        usuarios = json.load(f)
    return usuarios


def peliculas():
    with open("jsons/peliculas.json", "r") as file:
        peliculas = json.load(file)
    return peliculas

def comentarios():
    with open("jsons/comentarios.json") as r:
        comentarios = json.load(r)
    return comentarios
