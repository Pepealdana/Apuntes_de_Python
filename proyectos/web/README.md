# Proyecto web: lista de tareas con Flask

Archivo: [app_tareas_flask.py](app_tareas_flask.py)

## Funciones
- Agregar tareas con validación de longitud.
- Consultar la lista.
- Marcar tareas como completadas o volver a abrirlas.
- Eliminar tareas.
- Guardar la información en JSON para conservarla entre ejecuciones.

## Preparación
Desde la raíz del repositorio:

```bash
python -m venv .venv
python -m pip install flask
python proyectos/web/app_tareas_flask.py
```

Abre en el navegador la dirección local que muestra la terminal. Detén el servidor con Ctrl+C.

## Límites
Es una práctica local, no una aplicación lista para producción. No tiene autenticación, protección CSRF dedicada, base de datos multiusuario ni controles para despliegue público. No la expongas a internet ni guardes información sensible.

## Retos
1. Añade una fecha de creación.
2. Añade un filtro para ver tareas completas o pendientes.
3. Extrae la plantilla a un archivo HTML dentro de `templates/`.
4. Añade pruebas para las funciones de carga y guardado.
5. Sustituye JSON por SQLite cuando necesites consultas más complejas.

**Estado:** código incorporado; deben ejecutarse pruebas locales de rutas y persistencia antes de considerar la aplicación validada.
