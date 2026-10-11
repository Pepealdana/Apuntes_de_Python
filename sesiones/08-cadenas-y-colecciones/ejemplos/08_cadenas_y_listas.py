"""Sesión 8: operaciones con cadenas y listas."""


def main():
    nombre = "  ana aldana  "
    print("Nombre original:", repr(nombre))
    print("Nombre limpio:", nombre.strip().title())
    print()

    palabra = "Python"
    print("Primera letra:", palabra[0])
    print("Última letra:", palabra[-1])
    print("Cantidad de caracteres:", len(palabra))
    print()

    materiales = ["LED", "resistencia", "cable"]
    materiales.append("protoboard")
    print("Materiales:")
    for material in materiales:
        print("-", material)

    print("¿Hay cable?", "cable" in materiales)
    materiales.remove("cable")
    print("Lista final:", materiales)
    print()

    texto = "programacion"
    vocales = "aeiou"
    cantidad_vocales = 0
    for letra in texto.lower():
        if letra in vocales:
            cantidad_vocales += 1
    print(f"La palabra '{texto}' tiene {cantidad_vocales} vocales.")


if __name__ == "__main__":
    main()
