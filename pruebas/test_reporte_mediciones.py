"""Pruebas unitarias de la lectura y el resumen de mediciones."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "proyectos" / "datos"))
from reporte_mediciones import leer_mediciones, escribir_informe  # noqa: E402


class PruebasReporteMediciones(unittest.TestCase):
    def test_lee_valores_validos_y_registra_filas_invalidas(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "datos.csv"
            with ruta.open("w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["fecha", "grupo", "medicion"])
                escritor.writerow(["2026-01-01", "A", "2.5"])
                escritor.writerow(["2026-01-02", "A", "dato"])
                escritor.writerow(["2026-01-03", "B", ""])

            registros, errores = leer_mediciones(ruta)
            self.assertEqual(len(registros), 1)
            self.assertEqual(registros[0]["medicion"], 2.5)
            self.assertEqual(len(errores), 2)

    def test_omite_valores_no_finitos(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "datos.csv"
            ruta.write_text(
                "fecha,grupo,medicion\n2026-01-01,A,2.5\n2026-01-02,A,nan\n2026-01-03,A,inf\n",
                encoding="utf-8",
            )
            registros, errores = leer_mediciones(ruta)
            self.assertEqual(len(registros), 1)
            self.assertEqual(len(errores), 2)

    def test_falla_si_faltan_columnas_obligatorias(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "datos.csv"
            ruta.write_text("fecha,grupo\n2026-01-01,A\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                leer_mediciones(ruta)

    def test_genera_resumen_csv_e_informe(self):
        with tempfile.TemporaryDirectory() as temporal:
            registros = [
                {"fecha": "2026-01-01", "grupo": "A", "medicion": 2.0},
                {"fecha": "2026-01-02", "grupo": "A", "medicion": 4.0},
            ]
            resumen, informe = escribir_informe(registros, [], Path(temporal) / "salida")
            self.assertTrue(resumen.is_file())
            self.assertIn("promedio", resumen.read_text(encoding="utf-8"))
            self.assertIn("promedio=3.00", informe.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
