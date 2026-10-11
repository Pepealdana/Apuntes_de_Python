"""Comprueba que los enlaces relativos de los Markdown apunten a archivos existentes."""
import re
import unittest
from pathlib import Path
from urllib.parse import unquote

RAIZ = Path(__file__).resolve().parents[1]
PATRON_ENLACE = re.compile(r"!?[[^]]*]((<[^>]+>|[^)]+))")


class PruebasEnlacesDocumentacion(unittest.TestCase):
    def test_enlaces_internos_resuelven(self):
        errores = []
        archivos_markdown = sorted(RAIZ.rglob("*.md"))

        for archivo in archivos_markdown:
            contenido = archivo.read_text(encoding="utf-8")
            for coincidencia in PATRON_ENLACE.finditer(contenido):
                destino = coincidencia.group(1).strip()
                if destino.startswith("<") and destino.endswith(">"):
                    destino = destino[1:-1]
                destino = destino.split("#", 1)[0].split("?", 1)[0].strip()
                if not destino or destino.startswith(("#", "//")):
                    continue
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", destino):
                    continue

                destino = unquote(destino)
                ruta_destino = (archivo.parent / destino).resolve()
                if not ruta_destino.exists():
                    linea = contenido.count("\n", 0, coincidencia.start()) + 1
                    errores.append(
                        f"{archivo.relative_to(RAIZ)}:{linea} -> {destino}"
                    )

        self.assertEqual(
            errores,
            [],
            "Se encontraron enlaces internos rotos:\n" + "\n".join(errores),
        )


if __name__ == "__main__":
    unittest.main()
