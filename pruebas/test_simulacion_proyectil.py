"""Pruebas de la función matemática de trayectoria."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "proyectos" / "ciencia"))
from simulacion_proyectil import calcular_trayectoria  # noqa: E402


class PruebasTrayectoria(unittest.TestCase):
    def test_trayectoria_empieza_y_termina_en_el_suelo(self):
        puntos = calcular_trayectoria(20, 45, puntos=11)
        self.assertEqual(len(puntos), 11)
        self.assertAlmostEqual(puntos[0]["x_m"], 0.0)
        self.assertAlmostEqual(puntos[0]["y_m"], 0.0)
        self.assertAlmostEqual(puntos[-1]["y_m"], 0.0)
        self.assertGreater(puntos[-1]["x_m"], 0.0)
        self.assertGreater(max(p["y_m"] for p in puntos), 0.0)

    def test_rechaza_parametros_invalidos(self):
        with self.assertRaises(ValueError):
            calcular_trayectoria(0, 45)
        with self.assertRaises(ValueError):
            calcular_trayectoria(10, 90)
        with self.assertRaises(ValueError):
            calcular_trayectoria(10, 45, puntos=1)


if __name__ == "__main__":
    unittest.main()
