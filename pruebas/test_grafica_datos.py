"""Pruebas de lectura y generación de gráficas a partir de CSV."""
import csv
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("MPLBACKEND", "Agg")
RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "proyectos" / "datos"))
import grafica_datos  # noqa: E402


class PruebasGraficaDatos(unittest.TestCase):
    def crear_csv(self, ruta):
        with ruta.open("w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["fecha", "grupo", "medicion"])
            escritor.writerow(["2026-01-01", "A", "2.5"])
            escritor.writerow(["2026-01-02", "A", "dato-invalido"])
            escritor.writerow(["2026-01-03", "B", "4"])

    def test_lee_series_y_detecta_filas_invalidas(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "mediciones.csv"
            self.crear_csv(ruta)
            series, errores = grafica_datos.leer_series(ruta)
            self.assertEqual(series["A"], [("2026-01-01", 2.5)])
            self.assertEqual(series["B"], [("2026-01-03", 4.0)])
            self.assertEqual(len(errores), 1)

    def test_genera_archivo_de_grafica(self):
        with tempfile.TemporaryDirectory() as temporal:
            carpeta = Path(temporal)
            entrada = carpeta / "mediciones.csv"
            salida = carpeta / "grafica.png"
            self.crear_csv(entrada)
            with patch("sys.argv", ["grafica_datos.py", str(entrada), "--salida", str(salida)]):
                grafica_datos.main()
            self.assertTrue(salida.is_file())
            self.assertGreater(salida.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
