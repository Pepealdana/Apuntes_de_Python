"""Sesión 3: solicitar y usar datos de entrada."""


def main():
    nombre = input("¿Cómo te llamas? ")
    ciudad = input("¿En qué ciudad vives? ")
    print(f"Hola, {nombre}. Saludos hasta {ciudad}.")
    print()

    edad_texto = input("¿Cuántos años tienes? ")
    edad = int(edad_texto)
    print(f"El próximo año tendrás {edad + 1} años.")

    print()
    print("Recuerda: input() entrega texto; int() lo convierte a entero.")


if __name__ == "__main__":
    main()
