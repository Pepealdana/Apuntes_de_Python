# Sesión 1. Sintaxis, variables y tipos de datos

**Nivel:** inicial  
**Requisitos previos:** ninguno  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto de la sesión:** un programa que almacena y presenta información de manera clara.

## Objetivo de aprendizaje

Reconocer la sintaxis básica de Python, utilizar comentarios, crear variables y distinguir los tipos de datos `int`, `float`, `bool` y `str`.

## 1. Conceptos clave

### Sintaxis

La sintaxis es el conjunto de reglas que determina cómo se escribe un programa. Python distingue mayúsculas y minúsculas: `nombre` y `Nombre` son variables diferentes.

### Comentarios

Un comentario comienza con `#`. Python lo ignora al ejecutar el programa.

```python
# Este comentario explica la siguiente instrucción.
nombre = "Peters"
```

Las comillas triples (`'''...'''` o `"""..."""`) crean cadenas multilínea. No son comentarios por sí mismas; pueden utilizarse como documentación cuando ocupan la posición adecuada, por ejemplo al inicio de un módulo o función.

### Variables

Una variable es un nombre asociado a un valor. En Python no es necesario declarar por adelantado el tipo.

```python
nombre = "Peters"
edad = 40
estatura_m = 1.78
esta_activo = True
```

Los valores y nombres anteriores son ejemplos; cámbialos por datos ficticios propios para practicar.

### Tipos de datos iniciales

| Tipo | Para qué sirve | Ejemplo |
|---|---|---|
| `int` | Números enteros | `edad = 17` |
| `float` | Números con decimales | `temperatura = 23.5` |
| `bool` | Valores lógicos | `esta_encendido = True` |
| `str` | Texto | `ciudad = "Madrid"` |

Los valores booleanos se escriben exactamente `True` y `False`, con inicial mayúscula.

### Reglas sencillas para nombres

- Usa nombres que expliquen el dato: `temperatura`, no `x`, cuando el contexto lo permita.
- No empieces un nombre con un número.
- No uses espacios; separa palabras con guion bajo: `nombre_estudiante`.
- Evita palabras reservadas de Python y nombres incorporados como `str`, `list` o `sum`.

## 2. Ejemplo guiado

Abre y ejecuta [01_sintaxis_variables.py](ejemplos/01_sintaxis_variables.py).

Antes de ejecutarlo, predice qué tipo de dato corresponde a cada variable. Después compara tu predicción con la salida de `type()`.

## 3. Práctica paso a paso

1. Crea una variable de texto llamada `proyecto`.
2. Crea una variable entera llamada `numero_sensores`.
3. Crea una variable decimal llamada `temperatura`.
4. Crea una variable booleana llamada `sistema_activo`.
5. Muestra cada valor con `print()`.
6. Utiliza `type()` para comprobar el tipo de cada variable.

## 4. Retos

### Reto 1 — Ficha de presentación

Crea variables para representar un nombre ficticio, una asignatura, el número de estudiantes y si el proyecto está terminado. Muestra una ficha legible en la terminal.

### Reto 2 — Predice antes de ejecutar

Sin ejecutar el programa, escribe qué crees que devolverá `type()` para:

```python
cantidad = 12
promedio = 4.5
mensaje = "Hola"
terminado = False
```

Después ejecútalo y comprueba tus respuestas.

### Reto 3 — Detecta y corrige

Explica qué está mal en cada línea y corrígela:

```python
2estudiantes = 25
activo = true
ciudad = Madrid
```

## 5. Errores frecuentes

- Escribir `true` o `false` en minúscula.
- Olvidar las comillas de un texto.
- Empezar el nombre de una variable con un número.
- Confundir el valor de una variable con su nombre.
- Creer que las comillas triples siempre son comentarios.
- Usar nombres incorporados de Python como variables.

## 6. Cierre

Responde con tus propias palabras:

1. ¿Qué diferencia hay entre una variable y un valor?
2. ¿Cuándo usarías `int`, `float`, `bool` y `str`?
3. ¿Para qué sirve un comentario?
4. ¿Qué error te costó más identificar?

## Criterios de logro

- [ ] Puedo crear variables con nombres claros.
- [ ] Puedo distinguir los cuatro tipos de datos iniciales.
- [ ] Puedo mostrar valores con `print()`.
- [ ] Puedo comprobar tipos con `type()`.
- [ ] Puedo detectar errores básicos de sintaxis.

## Próxima sesión

**Mostrar información con `print()`:** presentar texto, variables y expresiones de manera clara.
