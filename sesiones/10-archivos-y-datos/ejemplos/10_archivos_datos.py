"""Sesión 10: guardar información en TXT, CSV y JSON."""

import csv
import json
from pathlib import Path


def main():
    carpeta_salida = Path("salida_sesion10")
    carpeta_salida.mkdir(exist_ok=True)

    archivo_texto = carpeta_salida / "notas.txt"
    with archivo_texto.open("w", encoding="utf-8") as archivo:
        archivo.write("Estoy aprendiendo a guardar información.\n")
        archivo.write("Los archivos permanecen después de cerrar el programa.\n")

    archivo_csv = carpeta_salida / "mediciones.csv"
    with archivo_csv.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["sensor", "temperatura_c"])
        escritor.writerow(["A1", 23.5])
        escritor.writerow(["A2", 24.1])

    configuracion = {
        "proyecto": "Estación escolar",
        "activa": True,
        "tareas": ["medir", "registrar", "analizar"],
    }
    archivo_json = carpeta_salida / "configuracion.json"
    with archivo_json.open("w", encoding="utf-8") as archivo:
        json.dump(configuracion, archivo, ensure_ascii=False, indent=2)

    print("Archivos creados en:", carpeta_salida.resolve())
    print("Contenido del archivo de texto:")
    print(archivo_texto.read_text(encoding="utf-8"))
    print("Configuración leída desde JSON:")
    with archivo_json.open("r", encoding="utf-8") as archivo:
        datos_leidos = json.load(archivo)
    print(datos_leidos)


if __name__ == "__main__":
    main()
