# Sesión 7. Repetir acciones con ciclos

**Nivel:** inicial  
**Requisitos previos:** sesiones 1 a 6  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto:** un programa que repite tareas de manera controlada.

## Objetivo

Usar los ciclos `for` y `while`, comprender los rangos y evitar ciclos que no terminan.

## 1. Conceptos clave

### Ciclo `for`

Se utiliza para recorrer elementos de una secuencia o repetir una acción un número conocido de veces.

```python
for numero in range(1, 6):
    print(numero)
```

Este ejemplo muestra 1, 2, 3, 4 y 5. El límite final de `range()` no se incluye.

`range(inicio, fin, paso)` permite definir el comienzo, el límite exclusivo y el incremento. Por ejemplo, `range(0, 10, 2)` produce 0, 2, 4, 6 y 8.

### Ciclo `while`

Repite un bloque mientras una condición sea verdadera.

```python
contador = 1

while contador <= 3:
    print("Intento", contador)
    contador += 1
```

Es importante actualizar las variables que controlan la condición; de lo contrario, el ciclo podría no terminar.

### Acumuladores y contadores

Un contador registra cuántas veces ocurre algo. Un acumulador suma valores a medida que avanza el ciclo.

```python
total = 0

for numero in range(1, 4):
    total += numero

print(total)  # 6
```

### Control del ciclo

- `break` termina el ciclo actual.
- `continue` salta al siguiente ciclo.

Se deben usar solo cuando hacen el programa más claro.

## 2. Ejemplo guiado

Ejecuta [07_ciclos.py](ejemplos/07_ciclos.py). Predice el total antes de ejecutarlo.

## 3. Experimenta

1. Cambia el límite de `range(1, 6)`.
2. Prueba `range(0, 11, 2)`.
3. Cambia el valor inicial y la condición del `while`.
4. Quita temporalmente `contador += 1` y explica el riesgo. No dejes un ciclo infinito ejecutándose.

## 4. Retos

### Reto 1 — Tabla de multiplicar

Solicita un número y muestra su tabla del 1 al 10.

### Reto 2 — Suma de una serie

Calcula la suma de los números del 1 hasta un número entero elegido por la persona.

### Reto 3 — Adivina el número

Usa `random.randint()` para elegir un número entre 1 y 20. Permite intentos con un ciclo `while`, indicando si el intento es mayor o menor. La validación avanzada de entradas se verá más adelante.

## 5. Errores frecuentes

- Pensar que `range(1, 5)` incluye el 5.
- Olvidar los dos puntos o la indentación.
- No cambiar la condición de un `while`.
- Reiniciar el acumulador dentro del ciclo cuando debe conservar su valor.
- Usar un ciclo cuando una operación sencilla bastaría.

## 6. Cierre

1. ¿Cuándo elegirías `for` y cuándo `while`?
2. ¿Qué diferencia hay entre contador y acumulador?
3. ¿Qué garantiza que un ciclo `while` termine?

## Criterios de logro

- [ ] Uso `for` con `range()`.
- [ ] Construyo un ciclo `while` con condición de salida.
- [ ] Calculo totales mediante un acumulador.
- [ ] Puedo explicar el riesgo de un ciclo infinito.

## Próxima sesión

**Cadenas y colecciones:** almacenar y recorrer grupos de datos.
