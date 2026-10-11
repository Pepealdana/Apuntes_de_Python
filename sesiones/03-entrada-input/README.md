# Sesión 3. Recibir información con `input()`

**Nivel:** inicial  
**Requisitos previos:** sesiones 1 y 2  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto:** un programa interactivo que solicita datos y responde.

## Objetivo

Solicitar información mediante `input()`, guardarla en variables y presentarla con `print()` y cadenas f.

## 1. Conceptos clave

### Leer texto

`input()` muestra una pregunta opcional y espera que la persona escriba una respuesta y pulse Intro. El resultado es una cadena (`str`), incluso si se escriben números.

```python
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}")
```

### Leer números

Para realizar operaciones matemáticas, convierte la entrada al tipo necesario:

```python
edad = int(input("¿Cuántos años tienes? "))
print(f"El próximo año tendrás {edad + 1}.")
```

Para números decimales se puede usar `float()`:

```python
temperatura = float(input("Temperatura en °C: "))
print(f"Registraste {temperatura} °C.")
```

Si la persona escribe texto donde se espera un número, `int()` o `float()` pueden generar `ValueError`. La validación y el manejo de errores se estudiarán más adelante; por ahora escribe una entrada válida.

### Usar la entrada directamente en una pregunta

`input("Pregunta: ")` muestra el texto y recibe la respuesta en la misma línea. No es necesario imprimir la pregunta por separado.

## 2. Ejemplo guiado

Ejecuta [03_input_interactivo.py](ejemplos/03_input_interactivo.py). Prueba primero una entrada de texto y después una entrada numérica.

## 3. Experimenta

1. Cambia las preguntas para que correspondan a un proyecto escolar.
2. Guarda la respuesta en una variable y muestra una frase personalizada.
3. Compara `numero = input(...)` con `numero = int(input(...))`.
4. Predice qué ocurre si intentas sumar `"10" + "2"` y qué ocurre con `10 + 2`.

## 4. Retos

### Reto 1 — Saludo personalizado

Solicita el nombre y la ciudad de una persona y presenta un saludo.

### Reto 2 — Edad futura

Solicita la edad como entero y calcula cuántos años tendrá dentro de cinco años.

### Reto 3 — Calculadora de suma

Solicita dos números enteros, conviértelos con `int()` y muestra la suma. Prueba también qué sucede con una entrada decimal y explica por qué.

## 5. Errores frecuentes

- Creer que `input()` devuelve automáticamente un número.
- Olvidar convertir el dato antes de hacer una operación numérica.
- Escribir `int` sin paréntesis o usar una conversión que no corresponde.
- Olvidar las llaves de una variable dentro de una cadena f.

## 6. Cierre

- ¿Qué tipo de dato devuelve `input()`?
- ¿Para qué sirven `int()` y `float()`?
- ¿Qué información necesita un programa para responder de manera personalizada?

## Criterios de logro

- [ ] Solicito datos con `input()`.
- [ ] Guardo las respuestas en variables.
- [ ] Muestro respuestas personalizadas.
- [ ] Convierto entradas numéricas cuando es necesario.

## Próxima sesión

**Operadores:** usar los datos para calcular y comparar resultados.
