"""Redimensiona una imagen y guarda una copia proporcional.

Instalación:
    python -m pip install pillow

Uso:
    python proyectos/imagenes/redimensionar_imagen.py foto.jpg --ancho 400
"""
import argparse
from pathlib import Path

from PIL import Image, ImageOps


def redimensionar(origen, ancho, salida, sobrescribir=False):
    if ancho < 1:
        raise ValueError("El ancho debe ser un entero positivo.")
    if not origen.is_file():
        raise FileNotFoundError(f"No existe la imagen: {origen}")
    salida.mkdir(parents=True, exist_ok=True)
    destino = salida / f"{origen.stem}_redimensionada{origen.suffix.lower()}"
    if destino.exists() and not sobrescribir:
        raise FileExistsError(f"El destino ya existe: {destino}. Usa --sobrescribir para reemplazarlo.")

    with Image.open(origen) as original:
        imagen = ImageOps.exif_transpose(original)
        if imagen.width < 1 or imagen.height < 1:
            raise ValueError("La imagen tiene dimensiones inválidas.")
        alto = max(1, round(imagen.height * ancho / imagen.width))
        copia = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
        if destino.suffix in {".jpg", ".jpeg"} and copia.mode not in {"RGB", "L"}:
            copia = copia.convert("RGB")
        copia.save(destino)
    return destino


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("imagen", type=Path, help="Ruta de la imagen original")
    parser.add_argument("--ancho", type=int, default=400, help="Ancho deseado en píxeles")
    parser.add_argument("--salida", type=Path, default=Path("imagenes_generadas"))
    parser.add_argument("--sobrescribir", action="store_true", help="Permite reemplazar la copia de salida")
    args = parser.parse_args()
    try:
        destino = redimensionar(args.imagen, args.ancho, args.salida, args.sobrescribir)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(f"Copia guardada en: {destino}")


if __name__ == "__main__":
    main()
