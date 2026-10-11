"""Lee un CSV de ejemplo y calcula un resumen sin paquetes externos.

Uso:
    python reporte_csv.py [ruta_al_archivo.csv]

Si no se proporciona una ruta, el programa crea y usa un CSV de ejemplo
en la carpeta actual. No modifica ni elimina archivos existentes.
"""

import csv
import math
import sys
from pathlib import Path


ARCHIVO_EJEMPLO = Path("mediciones_ejemplo.csv")
DATOS_EJEMPLO = [
    {"estudiante": "Estudiante A", "puntaje": "4.2"},
    {"estudiante": "Estudiante B", "puntaje": "3.8"},
    {"estudiante": "Estudiante C", "puntaje": "4.7"},
]


def crear_ejemplo_si_no_existe(ruta):
    """Crea datos ficticios solo si la ruta no existe."""
    if ruta.exists():
        return

    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["estudiante", "puntaje"])
        escritor.writeheader()
        escritor.writerows(DATOS_EJEMPLO)


def leer_puntajes(ruta):
    """Lee puntajes numéricos finitos y omite filas inválidas con aviso."""
    puntajes = []

    with ruta.open("r", newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        columnas = lector.fieldnames or []

        if "puntaje" not in columnas:
            raise ValueError("El CSV debe incluir una columna llamada 'puntaje'.")

        for numero_fila, fila in enumerate(lector, start=2):
            try:
                puntaje = float(fila["puntaje"])
                if not math.isfinite(puntaje):
                    raise ValueError("el puntaje debe ser finito")
                puntajes.append(puntaje)
            except (TypeError, ValueError) as error:
                print(f"Aviso: se omite el puntaje inválido de la fila {numero_fila}: {error}")

    return puntajes


def main():
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else ARCHIVO_EJEMPLO

    if len(sys.argv) == 1:
        crear_ejemplo_si_no_existe(ruta)

    if not ruta.is_file():
        print(f"No se encontró el archivo: {ruta}")
        return

    try:
        puntajes = leer_puntajes(ruta)
    except (OSError, ValueError) as error:
        print(f"No fue posible procesar el archivo: {error}")
        return

    if not puntajes:
        print("No hay puntajes válidos para resumir.")
        return

    print(f"Archivo: {ruta}")
    print(f"Registros válidos: {len(puntajes)}")
    print(f"Promedio: {sum(puntajes) / len(puntajes):.2f}")
    print(f"Mínimo: {min(puntajes):.2f}")
    print(f"Máximo: {max(puntajes):.2f}")


if __name__ == "__main__":
    main()
