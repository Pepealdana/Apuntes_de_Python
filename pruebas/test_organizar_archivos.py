"""Pruebas del plan de organización sin mover archivos."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "proyectos" / "automatizacion"))
from organizar_archivos import planificar  # noqa: E402


class PruebasOrganizador(unittest.TestCase):
    def test_planifica_sin_mover_archivos(self):
        with tempfile.TemporaryDirectory() as temporal:
            carpeta = Path(temporal)
            archivo = carpeta / "notas.txt"
            archivo.write_text("prueba", encoding="utf-8")

            plan = planificar(carpeta)

            self.assertEqual(len(plan), 1)
            self.assertEqual(plan[0][0], archivo)
            self.assertEqual(plan[0][1], carpeta / "txt" / "notas.txt")
            self.assertTrue(archivo.exists())
            self.assertFalse((carpeta / "txt").exists())

    def test_no_sobrescribe_destino_existente(self):
        with tempfile.TemporaryDirectory() as temporal:
            carpeta = Path(temporal)
            archivo = carpeta / "notas.txt"
            archivo.write_text("origen", encoding="utf-8")
            destino_dir = carpeta / "txt"
            destino_dir.mkdir()
            (destino_dir / "notas.txt").write_text("destino", encoding="utf-8")

            plan = planificar(carpeta)

            self.assertEqual(len(plan), 1)
            self.assertIsNone(plan[0][1])
            self.assertIn("ya existe", plan[0][2])
            self.assertEqual(archivo.read_text(encoding="utf-8"), "origen")


if __name__ == "__main__":
    unittest.main()
