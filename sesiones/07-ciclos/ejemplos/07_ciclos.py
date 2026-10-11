"""Sesión 7: ciclos for y while."""


def main():
    print("CONTEO")
    for numero in range(1, 6):
        print(numero)
    print()

    print("NÚMEROS PARES")
    for numero in range(0, 11, 2):
        print(numero, end=" ")
    print("\n")

    print("ACUMULADOR")
    total = 0
    for numero in range(1, 4):
        total += numero
    print("Suma del 1 al 3:", total)
    print()

    print("CICLO WHILE")
    contador = 1
    while contador <= 3:
        print("Intento", contador)
        contador += 1


if __name__ == "__main__":
    main()
