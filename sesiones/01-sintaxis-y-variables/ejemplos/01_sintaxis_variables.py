"""Sesión 1: sintaxis, variables y tipos de datos.

Ejemplo ejecutable para acompañar los apuntes del repositorio.
"""


def main():
    # Texto (str)
    nombre_proyecto = "Sistema de monitoreo"

    # Entero (int)
    numero_sensores = 3

    # Decimal (float)
    temperatura_c = 23.5

    # Booleano (bool): True o False, con inicial mayúscula
    sistema_activo = True

    print("FICHA DEL PROYECTO")
    print("------------------")
    print(f"Proyecto: {nombre_proyecto}")
    print(f"Número de sensores: {numero_sensores}")
    print(f"Temperatura: {temperatura_c} °C")
    print(f"¿Sistema activo?: {sistema_activo}")
    print()

    print("TIPOS DE DATOS")
    print(f"nombre_proyecto: {type(nombre_proyecto).__name__}")
    print(f"numero_sensores: {type(numero_sensores).__name__}")
    print(f"temperatura_c: {type(temperatura_c).__name__}")
    print(f"sistema_activo: {type(sistema_activo).__name__}")


if __name__ == "__main__":
    main()
