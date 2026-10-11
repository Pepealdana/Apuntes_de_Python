"""API REST local de tareas con Flask y almacenamiento JSON.

Instalación:
    python -m pip install flask
Ejecución:
    python proyectos/web/api_tareas.py

Demostración educativa local. No exponer a internet ni usar datos sensibles.
"""
import json
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)
ARCHIVO = Path("api_tareas.json")


def cargar():
    if not ARCHIVO.exists():
        return []
    with ARCHIVO.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list) or not all(isinstance(item, dict) for item in datos):
        raise ValueError("El archivo debe contener una lista de tareas.")
    return datos


def guardar(tareas):
    temporal = ARCHIVO.with_suffix(".json.tmp")
    with temporal.open("w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, ensure_ascii=False, indent=2)
    temporal.replace(ARCHIVO)


@app.errorhandler(json.JSONDecodeError)
def json_danado(_error):
    return jsonify(error="El archivo JSON está dañado; corrígelo antes de continuar."), 500


@app.errorhandler(OSError)
def error_archivo(_error):
    return jsonify(error="No fue posible leer o escribir el archivo de datos."), 500


@app.errorhandler(ValueError)
def error_datos(_error):
    return jsonify(error="La estructura del archivo de datos no es válida."), 500


@app.get("/api/tareas")
def listar_tareas():
    return jsonify(tareas=cargar())


@app.post("/api/tareas")
def crear_tarea():
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict):
        return jsonify(error="Envía un objeto JSON con la propiedad 'titulo'."), 400
    titulo = datos.get("titulo")
    if not isinstance(titulo, str) or not titulo.strip() or len(titulo.strip()) > 120:
        return jsonify(error="El título debe tener entre 1 y 120 caracteres."), 400

    tareas = cargar()
    nuevo_id = max((int(tarea.get("id", 0)) for tarea in tareas), default=0) + 1
    tarea = {"id": nuevo_id, "titulo": titulo.strip(), "hecha": False}
    tareas.append(tarea)
    guardar(tareas)
    return jsonify(tarea=tarea), 201


@app.patch("/api/tareas/<int:tarea_id>")
def actualizar_tarea(tarea_id):
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict):
        return jsonify(error="Envía un objeto JSON."), 400

    tareas = cargar()
    tarea = next((item for item in tareas if item.get("id") == tarea_id), None)
    if tarea is None:
        return jsonify(error="No existe una tarea con ese identificador."), 404

    if "titulo" in datos:
        titulo = datos["titulo"]
        if not isinstance(titulo, str) or not titulo.strip() or len(titulo.strip()) > 120:
            return jsonify(error="El título debe tener entre 1 y 120 caracteres."), 400
        tarea["titulo"] = titulo.strip()
    if "hecha" in datos:
        if not isinstance(datos["hecha"], bool):
            return jsonify(error="'hecha' debe ser true o false."), 400
        tarea["hecha"] = datos["hecha"]

    guardar(tareas)
    return jsonify(tarea=tarea)


@app.delete("/api/tareas/<int:tarea_id>")
def eliminar_tarea(tarea_id):
    tareas = cargar()
    restantes = [item for item in tareas if item.get("id") != tarea_id]
    if len(restantes) == len(tareas):
        return jsonify(error="No existe una tarea con ese identificador."), 404
    guardar(restantes)
    return jsonify(mensaje="Tarea eliminada.", id=tarea_id)


if __name__ == "__main__":
    app.run(debug=False)
