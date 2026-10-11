"""Pruebas de integración para la gráfica científica y el clasificador Iris."""
import contextlib
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("MPLBACKEND", "Agg")
RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "proyectos" / "ciencia"))
sys.path.insert(0, str(RAIZ / "proyectos" / "ia"))
import simulacion_proyectil  # noqa: E402
import clasificador_iris  # noqa: E402


class PruebasSimulacionProyectil(unittest.TestCase):
    def test_exporta_csv_y_grafica(self):
        with tempfile.TemporaryDirectory() as temporal:
            carpeta = Path(temporal)
            archivo_csv = carpeta / "trayectoria.csv"
            imagen = carpeta / "trayectoria.png"
            with patch("sys.argv", [
                "simulacion_proyectil.py", "--velocidad", "15",
                "--angulo", "40", "--csv", str(archivo_csv), "--imagen", str(imagen),
            ]):
                simulacion_proyectil.main()
            self.assertTrue(archivo_csv.is_file())
            self.assertTrue(imagen.is_file())
            self.assertGreater(imagen.stat().st_size, 0)
            self.assertIn("tiempo_s,x_m,y_m", archivo_csv.read_text(encoding="utf-8"))


class PruebasClasificadorIris(unittest.TestCase):
    def test_entrenamiento_y_reporte(self):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            clasificador_iris.main()
        texto = salida.getvalue()
        self.assertIn("CLASIFICACIÓN IRIS", texto)
        self.assertIn("Exactitud", texto)
        self.assertIn("Matriz de confusión", texto)
        self.assertIn("Reporte por clase", texto)


if __name__ == "__main__":
    unittest.main()
