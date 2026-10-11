"""Sesión 5: integrar variables, operaciones y salida."""


def main():
    animal = "oso"
    direccion_1 = "sur"
    direccion_2 = "este"
    direccion_3 = "norte"

    distancia_1 = 26
    distancia_2 = 19
    distancia_3 = 57

    distancia_total = distancia_1 + distancia_2 + distancia_3
    dos_primeros_tramos = distancia_1 + distancia_2
    diferencia_entre_primeros = distancia_1 - distancia_2

    print("LA HISTORIA DEL OSO")
    print()
    print(f"Un {animal} recorre {distancia_1} km hacia el {direccion_1}.")
    print(f"Después camina {distancia_2} km hacia el {direccion_2}.")
    print(f"Por último, recorre {distancia_3} km hacia el {direccion_3}.")
    print()
    print(f"Distancia total recorrida: {distancia_total} km.")
    print(f"Distancia de los dos primeros tramos: {dos_primeros_tramos} km.")
    print(
        "Diferencia entre los dos primeros tramos:",
        diferencia_entre_primeros,
        "km.",
    )
    print()
    print("¿Fue mayor el primer tramo que el segundo?", distancia_1 > distancia_2)


if __name__ == "__main__":
    main()
