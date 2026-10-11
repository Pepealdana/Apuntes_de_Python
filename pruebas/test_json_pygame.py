"""Pruebas de persistencia JSON y lógica básica de Pygame sin abrir ventanas."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "proyectos" / "interfaces"))
sys.path.insert(0, str(RAIZ / "proyectos" / "juegos"))
import gestor_actividades_json  # noqa: E402
import pygame_recolectar  # noqa: E402


class PruebasPersistenciaActividades(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.archivo = Path(self.temporal.name) / "actividades.json"
        self.parche = patch.object(gestor_actividades_json, "ARCHIVO", self.archivo)
        self.parche.start()
        self.addCleanup(self.parche.stop)
        self.addCleanup(self.temporal.cleanup)

    def test_guarda_y_recupera_datos_json(self):
        datos = [{"nombre": "Feria STEAM", "area": "Tecnología"}]
        gestor_actividades_json.guardar_actividades(datos)
        self.assertEqual(gestor_actividades_json.cargar_actividades(), datos)
        self.assertFalse(self.archivo.with_suffix(".json.tmp").exists())

    def test_rechaza_estructura_json_incorrecta(self):
        self.archivo.write_text('{"nombre": "no es una lista"}', encoding="utf-8")
        with self.assertRaises(ValueError):
            gestor_actividades_json.cargar_actividades()


class PruebasLogicaPygame(unittest.TestCase):
    def test_reiniciar_inicializa_jugador_obstaculos_y_estado(self):
        jugador, obstaculos, estrella, puntos, vidas, terminado = pygame_recolectar.reiniciar()
        self.assertEqual(len(obstaculos), 4)
        self.assertEqual(puntos, 0)
        self.assertEqual(vidas, pygame_recolectar.VIDAS_INICIALES)
        self.assertFalse(terminado)
        self.assertTrue(jugador.colliderect(pygame.Rect(0, 0, pygame_recolectar.ANCHO, pygame_recolectar.ALTO)))
        self.assertFalse(any(estrella.colliderect(obstaculo) for obstaculo in obstaculos))


if __name__ == "__main__":
    unittest.main()
