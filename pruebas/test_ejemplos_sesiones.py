"""Pruebas de humo para ejecutar los ejemplos de las doce sesiones."""
import contextlib
import io
import runpy
import unittest
from pathlib import Path
from unittest.mock import patch

RAIZ = Path(__file__).resolve().parents[1]
CARPETA_SESIONES = RAIZ / "sesiones"

ENTRADAS_POR_ARCHIVO = {
    "03_input_interactivo.py": ["Ada", "Bogotá", "15"],
    "11_excepciones.py": ["15", "10", "2"],
    "12_concurso_preguntas.py": ["B", "C", "A"],
}


class PruebasEjemplosDeSesiones(unittest.TestCase):
    def test_todos_los_ejemplos_se_ejecutan(self):
        ejemplos = sorted(CARPETA_SESIONES.glob("*/ejemplos/*.py"))
        self.assertEqual(len(ejemplos), 13, "Se esperaba conservar los 13 ejemplos originales de las sesiones.")

        for ejemplo in ejemplos:
            with self.subTest(ejemplo=ejemplo.relative_to(RAIZ)):
                entradas = ENTRADAS_POR_ARCHIVO.get(ejemplo.name, [])
                salida = io.StringIO()
                with patch("builtins.input", side_effect=entradas), contextlib.redirect_stdout(salida):
                    runpy.run_path(str(ejemplo), run_name="__main__")
                self.assertTrue(salida.getvalue().strip(), "El ejemplo debería producir una salida visible.")


if __name__ == "__main__":
    unittest.main()
