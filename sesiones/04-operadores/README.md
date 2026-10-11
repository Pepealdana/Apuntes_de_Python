# Sesión 4. Operadores en Python

**Nivel:** inicial  
**Requisitos previos:** sesiones 1, 2 y 3  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto:** un programa que realiza cálculos y compara datos.

## Objetivo

Utilizar operadores aritméticos, de comparación, asignación y pertenencia, y distinguir la igualdad de valores de la identidad de objetos.

## 1. Conceptos clave

Un operador permite realizar una operación con valores o variables. Las expresiones se evalúan y producen un resultado.

### 1.1 Operadores aritméticos

| Operador | Significado | Ejemplo | Resultado |
|---|---|---|---:|
| `+` | Suma | `10 + 3` | `13` |
| `-` | Resta | `10 - 3` | `7` |
| `*` | Multiplicación | `10 * 3` | `30` |
| `/` | División | `10 / 3` | `3.333...` |
| `//` | División entera hacia abajo | `10 // 3` | `3` |
| `%` | Residuo de la división | `10 % 3` | `1` |
| `**` | Potencia | `10 ** 3` | `1000` |

El operador `%` **no redondea decimales**: devuelve el residuo. Por ejemplo, 10 dividido entre 3 da cociente entero 3 y residuo 1.

### 1.2 Orden de las operaciones

En expresiones combinadas se aplican reglas de precedencia. Como orientación inicial:

1. Paréntesis.
2. Potencias.
3. Signos unarios, como el negativo.
4. Multiplicación, división, división entera y residuo.
5. Suma y resta.

```python
print(10 * (5 + 3))  # 80
print(10 * 5 + 3)    # 53
print(-2 ** 4)       # -16
print((-2) ** 4)     # 16
```

Usa paréntesis si hacen que la intención resulte más clara.

### 1.3 Operadores de comparación

Las comparaciones devuelven `True` o `False`.

| Operador | Significado |
|---|---|
| `==` | Igualdad de valores |
| `!=` | Desigualdad |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |

```python
print(30 > 10)       # True
print(20 < 10)       # False
print("hola" == "hola")  # True
print(20 >= 20)      # True
print(20 != 200)     # True
```

### 1.4 Operadores de asignación

La asignación guarda un valor en una variable. Los operadores compuestos actualizan el valor existente:

```python
puntos = 20
puntos += 10  # equivalente a puntos = puntos + 10
puntos -= 5   # equivalente a puntos = puntos - 5
puntos *= 2   # equivalente a puntos = puntos * 2
puntos /= 5   # equivalente a puntos = puntos / 5
print(puntos)
```

Después de `/=`, el resultado suele ser de tipo `float`, aunque la división sea exacta.

También se puede usar `+=` con listas para añadir elementos:

```python
numeros = [1, 2, 3]
numeros += [4, 5]
print(numeros)  # [1, 2, 3, 4, 5]
```

### 1.5 Identidad: `is` e `is not`

Estos operadores comprueban si dos referencias apuntan al **mismo objeto**, no si dos valores son iguales. Para comparar números o texto por su valor, normalmente se usa `==` o `!=`.

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True: tienen el mismo contenido
print(a is b)  # False: son listas distintas
```

No uses `is` para comprobar si dos números son iguales. Se utiliza habitualmente para comparaciones de identidad como `dato is None`.

### 1.6 Pertenencia: `in` y `not in`

Comprueban si un elemento aparece dentro de una secuencia o colección. En cadenas, la búsqueda distingue mayúsculas y minúsculas.

```python
numeros = [1, 2, 3, 4, 5]
print(3 in numeros)       # True
print(12 not in numeros) # True

mensaje = "Hello World"
print("World" in mensaje)  # True
print("world" in mensaje)  # False
```

## 2. Ejemplo guiado

Ejecuta [04_operadores.py](ejemplos/04_operadores.py). Observa los comentarios de cada operación y verifica los resultados.

## 3. Experimenta

1. Cambia `x = 10` y `y = 3` por otros valores.
2. Predice el resultado de `/`, `//` y `%` antes de ejecutar.
3. Cambia el orden de los paréntesis.
4. Compara dos listas con `==` y con `is`.
5. Prueba una búsqueda en texto con mayúsculas y minúsculas distintas.

## 4. Retos

### Reto 1 — Calculadora básica

Solicita dos números y muestra suma, resta, multiplicación y división. Para este reto, usa entradas válidas y evita dividir entre cero.

### Reto 2 — Comparar recorridos

Crea variables para tres distancias. Calcula el total, compara cuál es mayor y muestra los resultados con frases.

### Reto 3 — Presupuesto de una compra

Una persona tiene 12 monedas, presta 9, paga una deuda de 2 y encuentra 7. Si cada chocolate cuesta 2 monedas, calcula cuántas monedas le quedan y cuántos chocolates completos puede comprar. Distingue el total de monedas del número de chocolates.

### Reto 4 — Detecta el error conceptual

Explica por qué el siguiente código es una mala forma de comprobar igualdad numérica:

```python
a = 2
b = 2
print(a is b)
```

Reescríbelo con el operador adecuado.

## 5. Errores frecuentes

- Confundir `=` (asignar) con `==` (comparar).
- Decir que `%` redondea; en realidad devuelve el residuo.
- Confundir `//` con una división que siempre redondea hacia cero; con negativos, la división entera de Python redondea hacia abajo.
- Usar `is` para comparar valores.
- Sobrescribir nombres incorporados como `str`, `list` o `sum` con variables propias.
- Olvidar que `/=` modifica la variable y que la división produce un resultado de tipo `float`.

## 6. Cierre

- ¿Cuál es la diferencia entre `/`, `//` y `%`?
- ¿Qué diferencia hay entre `=` y `==`?
- ¿Cuándo usarías `in`?
- ¿Por qué `is` no es el operador apropiado para comparar dos números?

## Criterios de logro

- [ ] Realizo operaciones aritméticas.
- [ ] Predigo el orden de evaluación de expresiones sencillas.
- [ ] Comparo valores y explico el resultado booleano.
- [ ] Actualizo variables con operadores de asignación.
- [ ] Distingo igualdad, identidad y pertenencia.

## Próxima sesión

**Práctica integradora:** combinar variables, salida, entrada y operadores en un pequeño programa.
