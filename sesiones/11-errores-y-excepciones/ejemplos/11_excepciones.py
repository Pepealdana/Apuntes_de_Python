"""Sesión 11: manejo básico de excepciones."""


def leer_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print("Entrada no válida: escribe un número entero.")
        return None


def main():
    edad = leer_entero("¿Cuántos años tienes? ")
    if edad is not None:
        if edad < 0:
            print("La edad no puede ser negativa.")
        else:
            print(f"El próximo año tendrás {edad + 1} años.")

    print()
    try:
        dividendo = float(input("Dividendo: "))
        divisor = float(input("Divisor: "))
        if divisor == 0:
            print("No se puede dividir entre cero.")
        else:
            print("Resultado:", dividendo / divisor)
    except ValueError:
        print("Entrada no válida: escribe números.")


if __name__ == "__main__":
    main()
