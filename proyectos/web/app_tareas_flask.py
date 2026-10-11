"""Lista local de tareas con Flask y persistencia JSON.

Instalación: python -m pip install flask
Ejecución desde la raíz: python proyectos/web/app_tareas_flask.py

Es una demostración educativa local, no un servicio listo para publicar.
"""
import json
from pathlib import Path
from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)
ARCHIVO = Path("tareas_web.json")
PLANTILLA = """
<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lista de tareas</title>
<style>
body { max-width: 760px; margin: 2rem auto; padding: 0 1rem; font-family: system-ui,sans-serif; }
input[type=text] { padding: .6rem; width: min(65%,420px); }
button { padding: .55rem .8rem; cursor: pointer; }
li { display:flex; gap:1rem; align-items:center; justify-content:space-between; margin:.6rem 0; }
.hecha { text-decoration:line-through; opacity:.65; } .error { color:#a11; }
</style></head><body>
<h1>Lista de tareas</h1><p>Aplicación local de práctica. No introduzcas datos sensibles.</p>
{% if error %}<p class="error" role="alert">{{ error }}</p>{% endif %}
<form action="{{ url_for('agregar') }}" method="post">
<label for="titulo">Nueva tarea</label><br>
<input id="titulo" name="titulo" type="text" maxlength="120" required>
<button type="submit">Agregar</button></form>
{% if tareas %}<ul>{% for tarea in tareas %}<li>
<span class="{{ 'hecha' if tarea.hecha else '' }}">{{ tarea.titulo }}</span><span>
<form action="{{ url_for('alternar', tarea_id=tarea.id) }}" method="post" style="display:inline">
<button type="submit">{{ 'Reabrir' if tarea.hecha else 'Completar' }}</button></form>
<form action="{{ url_for('eliminar', tarea_id=tarea.id) }}" method="post" style="display:inline">
<button type="submit">Eliminar</button></form></span></li>{% endfor %}</ul>
{% else %}<p>No hay tareas registradas todavía.</p>{% endif %}
</body></html>
"""


def cargar_tareas():
    if not ARCHIVO.exists():
        return []
    with ARCHIVO.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list) or not all(isinstance(t, dict) for t in datos):
        raise ValueError("El archivo debe contener una lista de tareas.")
    return datos


def guardar_tareas(tareas):
    temporal = ARCHIVO.with_suffix(".json.tmp")
    with temporal.open("w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, ensure_ascii=False, indent=2)
    temporal.replace(ARCHIVO)


@app.get("/")
def inicio():
    try:
        tareas = cargar_tareas()
    except (OSError, json.JSONDecodeError, ValueError):
        return render_template_string(PLANTILLA, tareas=[], error="No se pudo leer tareas_web.json. Revisa el archivo antes de continuar."), 500
    return render_template_string(PLANTILLA, tareas=tareas, error=None)


@app.post("/agregar")
def agregar():
    titulo = request.form.get("titulo", "").strip()
    if not titulo or len(titulo) > 120:
        tareas = cargar_tareas()
        return render_template_string(PLANTILLA, tareas=tareas, error="El título debe tener entre 1 y 120 caracteres."), 400
    tareas = cargar_tareas()
    nuevo_id = max((int(t.get("id", 0)) for t in tareas), default=0) + 1
    tareas.append({"id": nuevo_id, "titulo": titulo, "hecha": False})
    guardar_tareas(tareas)
    return redirect(url_for("inicio"))


@app.post("/alternar/<int:tarea_id>")
def alternar(tarea_id):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea.get("id") == tarea_id:
            tarea["hecha"] = not bool(tarea.get("hecha", False))
            guardar_tareas(tareas)
            break
    return redirect(url_for("inicio"))


@app.post("/eliminar/<int:tarea_id>")
def eliminar(tarea_id):
    tareas = cargar_tareas()
    nuevas = [t for t in tareas if t.get("id") != tarea_id]
    if len(nuevas) != len(tareas):
        guardar_tareas(nuevas)
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=False)
