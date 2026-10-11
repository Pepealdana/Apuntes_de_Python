"""Solución guiada al reto de las monedas y los chocolates."""


def main():
    monedas_iniciales = 12
    monedas_prestadas = 9
    deuda_pagada = 2
    monedas_encontradas = 7
    precio_chocolate = 2

    monedas_finales = (
        monedas_iniciales
        - monedas_prestadas
        - deuda_pagada
        + monedas_encontradas
    )
    chocolates = monedas_finales // precio_chocolate
    monedas_sobrantes = monedas_finales % precio_chocolate

    print("Monedas disponibles:", monedas_finales)
    print("Chocolates que puede comprar:", chocolates)
    print("Monedas sobrantes:", monedas_sobrantes)


if __name__ == "__main__":
    main()
