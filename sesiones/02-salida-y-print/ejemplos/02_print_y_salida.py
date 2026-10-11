"""Sesión 2: mostrar información con print()."""


def main():
    nombre = "Ana"
    edad = 15
    proyecto = "Mini estación meteorológica"

    print("FICHA DE APRENDIZAJE")
    print("--------------------")
    print("Nombre:", nombre)
    print(f"Edad: {edad}")
    print(f"Proyecto: {proyecto}")
    print("En cinco años tendrá", edad + 5, "años.")
    print()

    print("Prueba de end:")
    print("Python", end=" | ")
    print("es práctico")
    print()

    print('Ella dijo: "Estoy aprendiendo Python".')
    print("Hola" "mundo")
    print("Hola", "mundo")


if __name__ == "__main__":
    main()
