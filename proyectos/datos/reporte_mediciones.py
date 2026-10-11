"""Lee mediciones CSV, valida filas y genera un informe de texto y CSV.

Uso desde la raíz del repositorio:
    python proyectos/datos/reporte_mediciones.py

Puedes pasar otra ruta como primer argumento. Los resultados se guardan
en la carpeta de salida indicada con --salida. Los datos del ejemplo son ficticios.
"""

import argparse
import csv
import math
from pathlib import Path
from statistics import mean


CSV_POR_DEFECTO = Path("proyectos/datos/mediciones_prueba.csv")


def leer_mediciones(ruta):
    registros = []
    errores = []
    with ruta.open("r", newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        requeridas = {"fecha", "grupo", "medicion"}
        if not requeridas.issubset(set(lector.fieldnames or [])):
            raise ValueError("El CSV debe incluir fecha, grupo y medicion.")

        for numero, fila in enumerate(lector, start=2):
            try:
                fecha = (fila.get("fecha") or "").strip()
                grupo = (fila.get("grupo") or "").strip()
                valor_texto = (fila.get("medicion") or "").strip().replace(",", ".")
                if not fecha or not grupo or not valor_texto:
                    raise ValueError("hay campos vacíos")
                valor = float(valor_texto)
                if not math.isfinite(valor):
                    raise ValueError("la medición debe ser un número finito")
                registros.append({"fecha": fecha, "grupo": grupo, "medicion": valor})
            except ValueError as error:
                errores.append(f"Fila {numero}: {error}")
    return registros, errores


def escribir_informe(registros, errores, salida):
    salida.mkdir(parents=True, exist_ok=True)
    archivo_resumen = salida / "resumen_mediciones.csv"
    archivo_texto = salida / "informe_mediciones.txt"

    grupos = {}
    for registro in registros:
        grupos.setdefault(registro["grupo"], []).append(registro["medicion"])

    with archivo_resumen.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["grupo", "cantidad", "promedio", "minimo", "maximo"])
        escritor.writeheader()
        for grupo, valores in sorted(grupos.items()):
            escritor.writerow({
                "grupo": grupo,
                "cantidad": len(valores),
                "promedio": f"{mean(valores):.2f}",
                "minimo": f"{min(valores):.2f}",
                "maximo": f"{max(valores):.2f}",
            })

    lineas = [
        "INFORME DE MEDICIONES",
        f"Registros válidos: {len(registros)}",
        f"Filas con problemas: {len(errores)}",
        "",
        "Resumen por grupo:",
    ]
    for grupo, valores in sorted(grupos.items()):
        lineas.append(
            f"- {grupo}: n={len(valores)}, promedio={mean(valores):.2f}, "
            f"mínimo={min(valores):.2f}, máximo={max(valores):.2f}"
        )
    if errores:
        lineas.extend(["", "Filas omitidas:"])
        lineas.extend(f"- {error}" for error in errores)

    archivo_texto.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return archivo_resumen, archivo_texto


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", type=Path, default=CSV_POR_DEFECTO, help="Ruta del CSV de entrada")
    parser.add_argument("--salida", type=Path, default=Path("salida_reporte"), help="Carpeta de resultados")
    args = parser.parse_args()

    try:
        registros, errores = leer_mediciones(args.csv)
        if not registros:
            print("No hay mediciones válidas; no se generó un resumen vacío.")
            for error in errores:
                print(f"Aviso: {error}")
            return
        resumen, informe = escribir_informe(registros, errores, args.salida)
    except (OSError, csv.Error, ValueError) as error:
        print(f"No se pudo procesar el archivo: {error}")
        return

    print(f"Mediciones válidas: {len(registros)}")
    print(f"Filas omitidas: {len(errores)}")
    print(f"Resumen: {resumen}")
    print(f"Informe: {informe}")


if __name__ == "__main__":
    main()
