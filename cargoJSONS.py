# Archivo secundario para traer los datos de los JSON y meterlos en diccionarios
import json
from flask import Flask, jsonify

# Cargo los datos de los usuarios desde un archivo JSON


def usuarios():
    with open("jsons/usuarios.json") as f:
        usuarios = json.load(f)
    return usuarios


def peliculas():
    with open("jsons/peliculas.json") as f:
        peliculas = json.load(f)
    return peliculas


def opiniones():
    with open("jsons/opiniones.json") as f:
        opiniones = json.load(f)
    return opiniones
