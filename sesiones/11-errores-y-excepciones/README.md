# Sesión 11. Errores, excepciones y validación

**Nivel:** inicial-intermedio  
**Requisitos previos:** sesiones 1 a 10  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto:** un programa que detecta entradas incorrectas y muestra mensajes comprensibles.

## Objetivo

Distinguir errores de sintaxis y errores durante la ejecución, y manejar excepciones frecuentes con `try` y `except`.

## 1. Conceptos clave

### Tres clases de problema

- **Error de sintaxis:** el código no puede interpretarse, por ejemplo por un paréntesis sin cerrar.
- **Error en ejecución:** el programa empieza, pero una operación falla, como convertir `"hola"` a entero.
- **Error lógico:** el programa se ejecuta, pero calcula o presenta un resultado incorrecto.

Los errores lógicos suelen requerir revisar los pasos, probar valores y comparar el resultado esperado con el real.

### Usar `try` y `except`

```python
try:
    edad = int(input("Edad: "))
except ValueError:
    print("Escribe la edad con números enteros.")
```

El bloque `try` contiene una operación que puede fallar. El bloque `except` gestiona un tipo de excepción concreto. Evita capturar todas las excepciones sin motivo: puede ocultar errores que necesitas encontrar.

### Validar antes de operar

```python
try:
    divisor = float(input("Divisor: "))
    if divisor == 0:
        print("No se puede dividir entre cero.")
    else:
        print(10 / divisor)
except ValueError:
    print("Debes escribir un número.")
```

### Mensajes útiles

Un buen mensaje explica qué dato se esperaba y cómo corregirlo, sin revelar información privada ni mostrar detalles técnicos innecesarios a la persona usuaria.

## 2. Ejemplo guiado

Ejecuta [11_excepciones.py](ejemplos/11_excepciones.py). Prueba entradas válidas, letras y el valor cero.

## 3. Experimenta

1. Cambia `int()` por `float()`.
2. Añade una segunda comprobación.
3. Provoca un error de conversión y observa si el programa continúa.
4. Compara el mensaje del programa con el traceback que aparece si no manejas la excepción.

## 4. Retos

### Reto 1 — Edad válida

Solicita una edad y gestiona la entrada que no se pueda convertir a entero.

### Reto 2 — División segura

Solicita dos números, controla la conversión y evita dividir por cero.

### Reto 3 — Leer archivo opcional

Intenta leer un archivo y gestiona `FileNotFoundError` con un mensaje que indique qué debe hacer la persona.

## 5. Errores frecuentes

- Usar `except:` sin indicar el tipo de excepción.
- Poner demasiadas operaciones dentro de un mismo `try`.
- Ocultar el error sin informar cómo corregirlo.
- Confundir la validación de datos con la corrección de errores lógicos.

## 6. Cierre

1. ¿Cómo distingues un error de sintaxis de uno lógico?
2. ¿Qué excepción puede ocurrir al convertir texto no numérico a entero?
3. ¿Por qué no conviene silenciar todos los errores?

## Criterios de logro

- [ ] Identifico errores de sintaxis, ejecución y lógica.
- [ ] Manejo `ValueError` en una entrada numérica.
- [ ] Compruebo una condición antes de hacer una operación peligrosa.
- [ ] Presento mensajes de error claros.

## Próxima sesión

**Mini proyecto de consola:** integrar entradas, condicionales, ciclos, funciones y manejo de errores.


## Práctica acumulativa — Proyecto: Aula organizada

Valida la cantidad, el costo unitario y la estructura de los datos leídos desde JSON. Maneja errores de conversión, archivo inexistente y JSON mal formado con mensajes útiles. Evita un `except` genérico que oculte cualquier problema.

**Criterio de revisión:** una entrada inválida no termina el programa de forma inesperada y los datos dañados no se reemplazan silenciosamente.

**Evidencia:** prueba texto en lugar de un número y un archivo JSON con contenido inválido; describe el mensaje obtenido.
