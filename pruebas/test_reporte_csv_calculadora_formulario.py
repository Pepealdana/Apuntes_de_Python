"""Pruebas de lógica y persistencia para proyectos de consola e interfaces."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "proyectos" / "automatizacion"))
sys.path.insert(0, str(RAIZ / "proyectos" / "interfaces"))

import reporte_csv  # noqa: E402
import calculadora_customtkinter  # noqa: E402
import formulario_estudiantes  # noqa: E402


class PruebasReporteCsv(unittest.TestCase):
    def test_crea_ejemplo_y_calcula_resumen(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "mediciones.csv"
            reporte_csv.crear_ejemplo_si_no_existe(ruta)
            puntajes = reporte_csv.leer_puntajes(ruta)
            self.assertEqual(len(puntajes), 3)
            self.assertAlmostEqual(sum(puntajes) / len(puntajes), 4.2333333333)

    def test_rechaza_csv_sin_columna_puntaje(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "incorrecto.csv"
            ruta.write_text("nombre,nota\nAna,4.5\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                reporte_csv.leer_puntajes(ruta)

    def test_omite_valores_no_finitos(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "mediciones.csv"
            ruta.write_text("estudiante,puntaje\nA,4.5\nB,nan\nC,inf\n", encoding="utf-8")
            puntajes = reporte_csv.leer_puntajes(ruta)
            self.assertEqual(puntajes, [4.5])


class PruebasLogicaCalculadora(unittest.TestCase):
    def test_operaciones_basicas(self):
        calcular = calculadora_customtkinter.calcular_operacion
        self.assertEqual(calcular(8, 2, "+"), 10)
        self.assertEqual(calcular(8, 2, "−"), 6)
        self.assertEqual(calcular(8, 2, "×"), 16)
        self.assertEqual(calcular(8, 2, "÷"), 4)

    def test_division_por_cero_operacion_desconocida_y_no_finitos(self):
        calcular = calculadora_customtkinter.calcular_operacion
        with self.assertRaises(ZeroDivisionError):
            calcular(8, 0, "÷")
        with self.assertRaises(ValueError):
            calcular(8, 2, "desconocida")
        with self.assertRaises(ValueError):
            calcular(float("nan"), 2, "+")


class PruebasPersistenciaFormulario(unittest.TestCase):
    def test_agrega_registros_y_encabezado_solo_una_vez(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "registros.csv"
            with patch.object(formulario_estudiantes, "ARCHIVO", ruta):
                formulario_estudiantes.guardar_registro({"nombre": "Ada", "curso": "10", "interes": "Robótica"})
                formulario_estudiantes.guardar_registro({"nombre": "Luis", "curso": "9", "interes": "Ciencia"})
            with ruta.open("r", newline="", encoding="utf-8") as archivo:
                filas = list(csv.DictReader(archivo))
            self.assertEqual(len(filas), 2)
            self.assertEqual(filas[0]["nombre"], "Ada")
            self.assertEqual(filas[1]["nombre"], "Luis")


if __name__ == "__main__":
    unittest.main()
