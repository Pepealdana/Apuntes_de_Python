"""Sesión 12: concurso de preguntas sin bibliotecas externas."""


PREGUNTAS = [
    {
        "pregunta": "¿Qué función muestra información en la consola?",
        "opciones": {"A": "input()", "B": "print()", "C": "type()"},
        "respuesta": "B",
    },
    {
        "pregunta": "¿Qué tipo de dato representa True o False?",
        "opciones": {"A": "str", "B": "float", "C": "bool"},
        "respuesta": "C",
    },
    {
        "pregunta": "¿Qué operador compara igualdad de valores?",
        "opciones": {"A": "==", "B": "=", "C": "is not"},
        "respuesta": "A",
    },
]


def presentar_pregunta(pregunta, numero):
    print(f"\nPregunta {numero}: {pregunta['pregunta']}")
    for letra, texto in pregunta["opciones"].items():
        print(f"  {letra}) {texto}")


def solicitar_respuesta():
    while True:
        respuesta = input("Tu respuesta (A, B o C): ").strip().upper()
        if respuesta in {"A", "B", "C"}:
            return respuesta
        print("Opción no válida. Escribe A, B o C.")


def ejecutar_concurso(preguntas):
    puntuacion = 0
    for numero, pregunta in enumerate(preguntas, start=1):
        presentar_pregunta(pregunta, numero)
        respuesta = solicitar_respuesta()
        if respuesta == pregunta["respuesta"]:
            print("Correcto.")
            puntuacion += 1
        else:
            print("No es correcto. La respuesta era", pregunta["respuesta"] + ".")
    return puntuacion


def main():
    print("CONCURSO DE PYTHON")
    print("Responde cada pregunta seleccionando A, B o C.")
    puntuacion = ejecutar_concurso(PREGUNTAS)
    total = len(PREGUNTAS)
    porcentaje = puntuacion / total * 100 if total else 0
    print("\nRESULTADO FINAL")
    print(f"Aciertos: {puntuacion} de {total}")
    print(f"Porcentaje: {porcentaje:.1f}%")


if __name__ == "__main__":
    main()
