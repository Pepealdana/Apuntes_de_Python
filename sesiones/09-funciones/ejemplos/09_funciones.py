"""Sesión 9: definir funciones, recibir argumentos y devolver resultados."""


def sumar(a, b):
    return a + b


def convertir_kilometros_a_metros(kilometros):
    return kilometros * 1000


def promedio(nota_1, nota_2, nota_3):
    return (nota_1 + nota_2 + nota_3) / 3


def main():
    resultado = sumar(4, 6)
    print("Suma:", resultado)
    print("7.5 km en metros:", convertir_kilometros_a_metros(7.5))
    print("Promedio:", promedio(4.0, 3.5, 4.5))


if __name__ == "__main__":
    main()
