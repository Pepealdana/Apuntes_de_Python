"""Organiza archivos por extensión; por defecto solo simula las acciones.

Ejemplos desde la raíz del repositorio:
    python proyectos/automatizacion/organizar_archivos.py carpeta_prueba
    python proyectos/automatizacion/organizar_archivos.py carpeta_prueba --aplicar

Usa primero una carpeta de prueba. El modo real mueve archivos y no se debe
aplicar a carpetas importantes sin revisar la simulación.
"""

import argparse
from pathlib import Path
import shutil


def planificar(carpeta):
    plan = []
    for archivo in sorted(carpeta.iterdir()):
        if not archivo.is_file():
            continue
        extension = archivo.suffix.lower().lstrip(".") or "sin_extension"
        destino_dir = carpeta / extension
        destino = destino_dir / archivo.name
        if destino_dir == archivo.parent:
            continue
        if destino.exists():
            plan.append((archivo, None, "omitido: ya existe el destino"))
        else:
            plan.append((archivo, destino, "mover"))
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("carpeta", type=Path, help="Carpeta de prueba que se organizará")
    parser.add_argument("--aplicar", action="store_true", help="Ejecutar los movimientos; sin esta opción solo simula")
    args = parser.parse_args()

    carpeta = args.carpeta.expanduser().resolve()
    if not carpeta.is_dir():
        parser.error(f"No existe una carpeta válida: {carpeta}")

    plan = planificar(carpeta)
    if not plan:
        print("No se encontraron archivos para organizar.")
        return

    print("MODO REAL" if args.aplicar else "SIMULACIÓN — no se cambiarán archivos")
    for origen, destino, accion in plan:
        if destino is None:
            print(f"{accion}: {origen.name}")
            continue
        print(f"{origen.name} -> {destino.relative_to(carpeta)}")
        if args.aplicar:
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(origen), str(destino))

    if not args.aplicar:
        print("Revisa el plan. Para mover los archivos, repite el comando con --aplicar.")


if __name__ == "__main__":
    main()
