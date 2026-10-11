"""Sesión 6: tomar decisiones con if, elif y else."""


def clasificar_temperatura(temperatura):
    if temperatura >= 30:
        return "Calor alto"
    elif temperatura >= 20:
        return "Temperatura moderada"
    else:
        return "Temperatura baja"


def main():
    temperatura = 27
    print("Temperatura:", temperatura, "°C")
    print(clasificar_temperatura(temperatura))
    print()

    nota = 4.2
    if nota >= 4.5:
        resultado = "Desempeño alto"
    elif nota >= 3.0:
        resultado = "Desempeño básico"
    else:
        resultado = "Debe reforzar el tema"
    print(f"Nota: {nota} — {resultado}")
    print()

    edad = 17
    tiene_permiso = True
    if edad >= 16 and tiene_permiso:
        print("Puede participar en esta actividad.")
    else:
        print("No cumple las condiciones de esta actividad.")


if __name__ == "__main__":
    main()
