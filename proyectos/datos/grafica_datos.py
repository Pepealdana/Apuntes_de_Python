"""Grafica mediciones de un CSV con Matplotlib.

Uso desde la raíz del repositorio:
    python proyectos/datos/grafica_datos.py
    python proyectos/datos/grafica_datos.py ruta/mediciones.csv

El CSV debe contener las columnas fecha, grupo y medicion.
"""
import argparse
import csv
from pathlib import Path
import matplotlib.pyplot as plt

CSV_POR_DEFECTO = Path("proyectos/datos/mediciones_prueba.csv")


def leer_series(ruta):
    series, errores = {}, []
    with ruta.open("r", newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        if not {"fecha", "grupo", "medicion"}.issubset(set(lector.fieldnames or [])):
            raise ValueError("El CSV debe incluir fecha, grupo y medicion.")
        for numero, fila in enumerate(lector, start=2):
            fecha = (fila.get("fecha") or "").strip()
            grupo = (fila.get("grupo") or "").strip()
            valor = (fila.get("medicion") or "").strip().replace(",", ".")
            try:
                if not fecha or not grupo or not valor:
                    raise ValueError("campos vacíos")
                numero_valor = float(valor)
            except ValueError as error:
                errores.append(f"Fila {numero}: {error}")
                continue
            series.setdefault(grupo, []).append((fecha, numero_valor))
    return series, errores


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", type=Path, default=CSV_POR_DEFECTO)
    parser.add_argument("--salida", type=Path, help="Ruta opcional para guardar la gráfica como imagen")
    args = parser.parse_args()
    try:
        series, errores = leer_series(args.csv)
    except (OSError, csv.Error, ValueError) as error:
        print(f"No se pudo leer el CSV: {error}")
        return
    if not series:
        print("No hay mediciones válidas para graficar.")
        for error in errores:
            print(f"Aviso: {error}")
        return
    for grupo, valores in sorted(series.items()):
        plt.plot([x[0] for x in valores], [x[1] for x in valores], marker="o", label=f"Grupo {grupo}")
    plt.title("Mediciones por fecha")
    plt.xlabel("Fecha")
    plt.ylabel("Medición (unidades del conjunto de prueba)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xticks(rotation=30)
    plt.tight_layout()
    if args.salida:
        args.salida.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(args.salida, dpi=150)
        print(f"Gráfica guardada en: {args.salida}")
    else:
        plt.show()
    if errores:
        print(f"Filas omitidas: {len(errores)}")
        for error in errores:
            print(f"Aviso: {error}")


if __name__ == "__main__":
    main()
