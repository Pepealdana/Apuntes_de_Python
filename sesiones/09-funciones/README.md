# Sesión 9. Crear funciones

**Nivel:** inicial  
**Requisitos previos:** sesiones 1 a 8  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto:** un programa dividido en funciones pequeñas que se pueden reutilizar.

## Objetivo

Definir y llamar funciones, usar parámetros y valores de retorno, y comprender el alcance básico de las variables.

## 1. Conceptos clave

### Definir y llamar una función

Una función agrupa instrucciones bajo un nombre. `def` la define; el cuerpo debe estar indentado. La función no se ejecuta hasta que se llama.

```python
def saludar():
    print("Hola")

saludar()
```

### Parámetros y argumentos

Los parámetros son los nombres que aparecen en la definición; los argumentos son los valores que se pasan al llamar la función.

```python
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Ana")
```

### Devolver un resultado

`return` entrega un resultado a quien llamó la función. No es lo mismo que imprimirlo.

```python
def sumar(a, b):
    return a + b

resultado = sumar(4, 6)
print(resultado)
```

Si una función no ejecuta `return`, devuelve `None` de manera predeterminada.

### Evitar repetir lógica

Si un cálculo se usa en varios lugares, conviene encapsularlo en una función. Las funciones deben tener nombres descriptivos y realizar una tarea clara.

### Alcance de las variables

Una variable creada dentro de una función es local a esa función. Para compartir información entre funciones, es preferible pasarla como argumento y devolver resultados, en lugar de depender de variables globales.

## 2. Ejemplo guiado

Ejecuta [09_funciones.py](ejemplos/09_funciones.py). Cambia los argumentos y observa cómo cambian los resultados.

## 3. Experimenta

1. Cambia los argumentos de `sumar()`.
2. Crea una función `doble(numero)` que devuelva el doble.
3. Crea una función que convierta grados Celsius a Fahrenheit.
4. Compara una función que usa `print()` con otra que usa `return`.

## 4. Retos

### Reto 1 — Conversor

Escribe una función que reciba kilómetros y devuelva metros.

### Reto 2 — Promedio

Crea una función que reciba tres notas y devuelva su promedio.

### Reto 3 — Reutiliza una función

Crea una función que reciba una lista de números y devuelva su suma. Pruébala con varias listas.

## 5. Errores frecuentes

- Definir una función pero nunca llamarla.
- Olvidar los paréntesis al llamarla.
- Confundir `return` con `print()`.
- No indentar el cuerpo.
- Intentar utilizar fuera de la función una variable local.

## 6. Cierre

1. ¿Qué diferencia hay entre parámetro y argumento?
2. ¿Qué devuelve una función?
3. ¿Cuándo es útil dividir un programa en funciones?

## Criterios de logro

- [ ] Defino y llamo funciones.
- [ ] Uso parámetros para recibir datos.
- [ ] Devuelvo resultados con `return`.
- [ ] Divido un problema en funciones pequeñas.

## Próxima sesión

**Archivos y datos persistentes:** guardar información para usarla después de cerrar el programa.
