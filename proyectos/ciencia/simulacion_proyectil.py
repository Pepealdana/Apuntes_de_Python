"""Simula una trayectoria ideal de proyectil y grafica sus resultados.

Instalación:
    python -m pip install matplotlib

Modelo introductorio: sin resistencia del aire, terreno horizontal y gravedad
constante. No es un simulador de ingeniería ni una predicción experimental.
"""
import argparse
import csv
import math
from pathlib import Path



GRAVEDAD = 9.81


def calcular_trayectoria(velocidad, angulo_grados, puntos=101):
    if velocidad <= 0:
        raise ValueError("La velocidad inicial debe ser positiva.")
    if not 0 < angulo_grados < 90:
        raise ValueError("El ángulo debe estar entre 0 y 90 grados.")
    if puntos < 2:
        raise ValueError("Se necesitan al menos dos puntos.")

    angulo = math.radians(angulo_grados)
    vx = velocidad * math.cos(angulo)
    vy = velocidad * math.sin(angulo)
    tiempo_total = 2 * vy / GRAVEDAD
    trayectoria = []
    for indice in range(puntos):
        tiempo = tiempo_total * indice / (puntos - 1)
        x = vx * tiempo
        y = vy * tiempo - 0.5 * GRAVEDAD * tiempo**2
        trayectoria.append({"tiempo_s": tiempo, "x_m": x, "y_m": max(0.0, y)})
    return trayectoria


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--velocidad", type=float, default=20.0, help="Velocidad inicial en m/s")
    parser.add_argument("--angulo", type=float, default=45.0, help="Ángulo inicial en grados")
    parser.add_argument("--csv", type=Path, default=Path("salida_ciencia/trayectoria.csv"))
    parser.add_argument("--imagen", type=Path, default=Path("salida_ciencia/trayectoria.png"))
    args = parser.parse_args()

    try:
        trayectoria = calcular_trayectoria(args.velocidad, args.angulo)
    except ValueError as error:
        parser.error(str(error))

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    args.imagen.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["tiempo_s", "x_m", "y_m"])
        escritor.writeheader()
        escritor.writerows(trayectoria)

    import matplotlib.pyplot as plt

    alcance = trayectoria[-1]["x_m"]
    altura = max(punto["y_m"] for punto in trayectoria)
    plt.plot([p["x_m"] for p in trayectoria], [p["y_m"] for p in trayectoria])
    plt.title("Trayectoria ideal de un proyectil")
    plt.xlabel("Distancia horizontal (m)")
    plt.ylabel("Altura (m)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(args.imagen, dpi=150)
    print(f"Alcance estimado: {alcance:.2f} m")
    print(f"Altura máxima aproximada: {altura:.2f} m")
    print(f"CSV: {args.csv}")
    print(f"Gráfica: {args.imagen}")


if __name__ == "__main__":
    main()
