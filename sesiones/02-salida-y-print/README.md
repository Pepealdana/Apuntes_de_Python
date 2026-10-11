# Sesión 2. Mostrar información con `print()`

**Nivel:** inicial  
**Requisitos previos:** sesión 1  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto:** un programa que presenta información de manera legible.

## Objetivo

Usar `print()` para mostrar texto, variables y expresiones; controlar los saltos de línea y escribir comillas dentro de una cadena.

## 1. Conceptos clave

### Mostrar un mensaje

`print()` muestra información en la salida del programa:

```python
print("Hola")
print("Estoy aprendiendo Python")
```

### Mostrar varios valores

Se pueden separar los argumentos con comas. Python inserta un espacio entre ellos de forma predeterminada.

```python
nombre = "Ana"
edad = 15
print("Nombre:", nombre)
print("Edad:", edad)
print("En cinco años tendrá", edad + 5)
```

También se pueden usar cadenas f:

```python
print(f"{nombre} tiene {edad} años.")
```

### Saltos de línea

Cada llamada a `print()` termina en una nueva línea. Un `print()` vacío genera una línea en blanco.

```python
print("Primera línea")
print()
print("Tercera línea")
```

El parámetro `end` cambia lo que se escribe al final. Por defecto es un salto de línea:

```python
print("Hola", end=" ")
print("mundo")
# Hola mundo
```

### Comillas dentro de cadenas

Si una cadena empieza y termina con comillas dobles, para incluir comillas dobles dentro de ella se pueden usar comillas simples alrededor o escapar las comillas internas:

```python
print('Ella dijo: "Hola"')
print("Ella dijo: \"Hola\"")
print("It's Python")
```

Las cadenas adyacentes escritas literalmente se unen, pero no agregan un espacio automáticamente:

```python
print("Hola" "mundo")  # Holamundo
print("Hola", "mundo") # Hola mundo
```

## 2. Ejemplo guiado

Ejecuta [02_print_y_salida.py](ejemplos/02_print_y_salida.py). Antes de ejecutarlo, predice cómo quedará cada línea.

## 3. Experimenta

1. Cambia el nombre y la edad del ejemplo.
2. Muestra tres variables en una misma llamada a `print()`.
3. Prueba `end=""`, `end=" "` y `end=" | "`.
4. Compara el resultado de `print("Hola" "Peters")` con `print("Hola", "Peters")`.

## 4. Retos

### Reto 1 — Tarjeta de presentación

Muestra nombre ficticio, curso, asignatura favorita y una meta de aprendizaje.

### Reto 2 — Mini cartel

Presenta el título de un proyecto, una línea en blanco, una descripción y el estado del proyecto.

### Reto 3 — Predice la salida

Sin ejecutar, escribe el resultado:

```python
print("A", "B", "C")
print("Uno", end="-")
print("Dos")
print("Py" "thon")
```

Después ejecuta y compara.

## 5. Errores frecuentes

- Olvidar cerrar comillas o paréntesis.
- Escribir comillas del mismo tipo dentro de una cadena sin escaparlas.
- Esperar que dos cadenas adyacentes incluyan un espacio.
- Confundir mostrar una variable con escribir su nombre dentro de una cadena normal.

## 6. Cierre

- ¿Qué diferencia hay entre separar argumentos con coma y escribir dos cadenas literales seguidas?
- ¿Qué hace el parámetro `end`?
- ¿Cuándo usarías una cadena f?

## Criterios de logro

- [ ] Muestro texto, variables y expresiones.
- [ ] Uso saltos de línea de forma intencional.
- [ ] Puedo combinar texto y variables.
- [ ] Puedo escribir comillas dentro de una cadena.

## Próxima sesión

**Entrada de datos con `input()`:** permitir que la persona interactúe con el programa.
