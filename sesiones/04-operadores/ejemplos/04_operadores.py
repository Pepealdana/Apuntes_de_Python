"""Sesión 4: ejemplos de operadores aritméticos, comparación y pertenencia."""


def main():
    x = 10
    y = 3

    print("OPERADORES ARITMÉTICOS")
    print("Suma:", x + y)
    print("Resta:", x - y)
    print("Multiplicación:", x * y)
    print("División:", x / y)
    print("División entera:", x // y)
    print("Residuo:", x % y)
    print("Potencia:", x ** y)
    print()

    print("ORDEN DE LAS OPERACIONES")
    print(10 * (5 + 3))  # 80
    print(10 * 5 + 3)    # 53
    print(-2 ** 4)       # -16
    print((-2) ** 4)     # 16
    print()

    print("COMPARACIONES")
    print("x > y:", x > y)
    print("x == y:", x == y)
    print("x != y:", x != y)
    print()

    puntos = 20
    puntos += 10
    puntos -= 5
    puntos *= 2
    puntos /= 5
    print("Puntos tras las asignaciones:", puntos)
    print()

    primera = [1, 2]
    segunda = [1, 2]
    print("Listas con el mismo contenido:", primera == segunda)
    print("¿Es el mismo objeto?:", primera is segunda)
    print()

    mensaje = "Hello World"
    print("'World' está en el texto:", "World" in mensaje)
    print("'world' está en el texto:", "world" in mensaje)


if __name__ == "__main__":
    main()
