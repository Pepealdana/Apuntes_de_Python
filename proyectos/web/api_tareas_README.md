# API REST de tareas con Flask

Archivo: [api_tareas.py](api_tareas.py)

## Preparación

```bash
python -m pip install flask
python proyectos/web/api_tareas.py
```

La API queda disponible en la dirección local indicada por Flask, normalmente `http://127.0.0.1:5000`. Los datos se guardan en `api_tareas.json` en el directorio de trabajo.

## Endpoints

| Método | Ruta | Función |
|---|---|---|
| GET | `/api/tareas` | Devuelve la lista de tareas |
| POST | `/api/tareas` | Crea una tarea a partir de JSON |
| PATCH | `/api/tareas/<id>` | Cambia el título o el estado |
| DELETE | `/api/tareas/<id>` | Elimina una tarea |

## Ejemplos con curl

Listar:

```bash
curl http://127.0.0.1:5000/api/tareas
```

Crear:

```bash
curl -X POST http://127.0.0.1:5000/api/tareas -H "Content-Type: application/json" -d "{\"titulo\":\"Preparar prototipo\"}"
```

Marcar como completada (cambia el identificador si es necesario):

```bash
curl -X PATCH http://127.0.0.1:5000/api/tareas/1 -H "Content-Type: application/json" -d "{\"hecha\":true}"
```

Eliminar:

```bash
curl -X DELETE http://127.0.0.1:5000/api/tareas/1
```

## Qué aprender

- Métodos HTTP y códigos de estado.
- JSON como formato de intercambio.
- Validación de datos entrantes.
- Diferencia entre una ruta de lectura y una que modifica información.
- Persistencia de datos y manejo de errores.

## Límites

Es una API didáctica de un solo proceso con archivo JSON, sin autenticación ni protección para despliegue público. No la expongas a internet ni guardes datos personales. En una aplicación real deben evaluarse autenticación, autorización, CSRF cuando corresponda, concurrencia, copias de seguridad y almacenamiento apropiado.

**Estado:** código incorporado; faltan pruebas locales de los endpoints y los casos de error.
