"""Pruebas funcionales de la aplicación web y la API REST con archivos temporales."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "proyectos" / "web"))

import api_tareas  # noqa: E402
import app_tareas_flask  # noqa: E402


class PruebasApiTareas(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.archivo = Path(self.temporal.name) / "tareas.json"
        self.parche = patch.object(api_tareas, "ARCHIVO", self.archivo)
        self.parche.start()
        self.addCleanup(self.parche.stop)
        self.addCleanup(self.temporal.cleanup)
        api_tareas.app.config.update(TESTING=True)
        self.cliente = api_tareas.app.test_client()

    def test_ciclo_crud_y_persistencia_json(self):
        self.assertEqual(self.cliente.get("/api/tareas").get_json(), {"tareas": []})

        creado = self.cliente.post("/api/tareas", json={"titulo": "Preparar robot"})
        self.assertEqual(creado.status_code, 201)
        tarea = creado.get_json()["tarea"]
        self.assertEqual(tarea["titulo"], "Preparar robot")
        self.assertTrue(self.archivo.is_file())

        actualizado = self.cliente.patch(f"/api/tareas/{tarea['id']}", json={"hecha": True})
        self.assertEqual(actualizado.status_code, 200)
        self.assertTrue(actualizado.get_json()["tarea"]["hecha"])
        self.assertTrue(json.loads(self.archivo.read_text(encoding="utf-8"))[0]["hecha"])

        eliminado = self.cliente.delete(f"/api/tareas/{tarea['id']}")
        self.assertEqual(eliminado.status_code, 200)
        self.assertEqual(self.cliente.get("/api/tareas").get_json(), {"tareas": []})

    def test_valida_payload_y_identificadores(self):
        self.assertEqual(self.cliente.post("/api/tareas", json={"titulo": " "}).status_code, 400)
        self.assertEqual(self.cliente.post("/api/tareas", json=["no es objeto"]).status_code, 400)
        self.assertEqual(self.cliente.patch("/api/tareas/999", json={"hecha": True}).status_code, 404)
        creado = self.cliente.post("/api/tareas", json={"titulo": "Leer"})
        tarea_id = creado.get_json()["tarea"]["id"]
        self.assertEqual(self.cliente.patch(f"/api/tareas/{tarea_id}", json={"hecha": "sí"}).status_code, 400)


class PruebasAplicacionWeb(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.archivo = Path(self.temporal.name) / "tareas_web.json"
        self.parche = patch.object(app_tareas_flask, "ARCHIVO", self.archivo)
        self.parche.start()
        self.addCleanup(self.parche.stop)
        self.addCleanup(self.temporal.cleanup)
        app_tareas_flask.app.config.update(TESTING=True)
        self.cliente = app_tareas_flask.app.test_client()

    def test_agrega_completa_y_elimina_tarea(self):
        respuesta = self.cliente.get("/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(b"No hay tareas", respuesta.data)

        creada = self.cliente.post("/agregar", data={"titulo": "Probar interfaz"}, follow_redirects=True)
        self.assertEqual(creada.status_code, 200)
        self.assertIn(b"Probar interfaz", creada.data)
        tarea = json.loads(self.archivo.read_text(encoding="utf-8"))[0]

        completada = self.cliente.post(f"/alternar/{tarea['id']}", follow_redirects=True)
        self.assertEqual(completada.status_code, 200)
        self.assertTrue(json.loads(self.archivo.read_text(encoding="utf-8"))[0]["hecha"])

        eliminada = self.cliente.post(f"/eliminar/{tarea['id']}", follow_redirects=True)
        self.assertEqual(eliminada.status_code, 200)
        self.assertEqual(json.loads(self.archivo.read_text(encoding="utf-8")), [])

    def test_rechaza_titulo_vacio(self):
        respuesta = self.cliente.post("/agregar", data={"titulo": "   "})
        self.assertEqual(respuesta.status_code, 400)


if __name__ == "__main__":
    unittest.main()
