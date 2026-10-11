"""Pruebas del procesamiento de imágenes sin usar archivos del usuario."""
import tempfile
import unittest
from pathlib import Path

from PIL import Image

import sys
RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "proyectos" / "imagenes"))
from redimensionar_imagen import redimensionar  # noqa: E402


class PruebasRedimensionarImagen(unittest.TestCase):
    def test_guarda_copia_con_proporcion_y_conserva_original(self):
        with tempfile.TemporaryDirectory() as temporal:
            carpeta = Path(temporal)
            origen = carpeta / "origen.png"
            Image.new("RGB", (120, 60), "white").save(origen)

            destino = redimensionar(origen, 40, carpeta / "salida")

            self.assertTrue(destino.is_file())
            with Image.open(destino) as imagen:
                self.assertEqual(imagen.size, (40, 20))
            with Image.open(origen) as original:
                self.assertEqual(original.size, (120, 60))

    def test_no_sobrescribe_sin_permiso_y_valida_ancho(self):
        with tempfile.TemporaryDirectory() as temporal:
            carpeta = Path(temporal)
            origen = carpeta / "origen.png"
            Image.new("RGB", (10, 10), "white").save(origen)
            salida = carpeta / "salida"
            destino = redimensionar(origen, 5, salida)
            with self.assertRaises(FileExistsError):
                redimensionar(origen, 5, salida)
            with self.assertRaises(ValueError):
                redimensionar(origen, 0, salida)
            self.assertTrue(destino.is_file())


if __name__ == "__main__":
    unittest.main()
