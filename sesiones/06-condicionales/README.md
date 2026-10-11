# Sesión 6. Tomar decisiones con condicionales

**Nivel:** inicial  
**Requisitos previos:** sesiones 1 a 5  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto:** un programa que responde de manera diferente según los datos recibidos.

## Objetivo

Usar `if`, `elif` y `else` para ejecutar instrucciones según se cumplan condiciones.

## 1. Conceptos clave

### Una decisión con `if`

La instrucción `if` ejecuta un bloque cuando una condición es verdadera. Los dos puntos y la indentación son obligatorios.

```python
temperatura = 28

if temperatura > 25:
    print("Hace calor")
```

### Alternativas con `else`

```python
edad = 16

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
```

### Varias opciones con `elif`

```python
nota = 4.2

if nota >= 4.5:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
else:
    print("Debe reforzar el tema")
```

Python evalúa las condiciones en orden y ejecuta solo el primer bloque cuya condición sea verdadera. Los rangos y sus etiquetas son ejemplos didácticos; adapta los criterios al contexto.

### Combinar condiciones

- `and`: ambas condiciones deben ser verdaderas.
- `or`: basta con que una sea verdadera.
- `not`: invierte el valor lógico.

```python
edad = 17
tiene_permiso = True

if edad >= 16 and tiene_permiso:
    print("Puede participar en esta actividad")
```

Usa paréntesis cuando ayuden a que una condición compleja se entienda.

### Comparar no es asignar

`=` asigna un valor; `==` compara dos valores. Una condición debe evaluar a un resultado lógico.

## 2. Ejemplo guiado

Ejecuta [06_condicionales.py](ejemplos/06_condicionales.py). Cambia la temperatura, la nota y el valor booleano para observar las diferentes rutas.

## 3. Experimenta

1. Cambia la condición de temperatura de `>` a `>=`.
2. Prueba una nota exactamente igual a 3.0.
3. Cambia `and` por `or` y explica cómo cambia la decisión.
4. Introduce una condición que nunca pueda cumplirse y explica por qué.

## 4. Retos

### Reto 1 — Número positivo, negativo o cero

Solicita un número y determina si es positivo, negativo o igual a cero.

### Reto 2 — Acceso a una actividad

Solicita la edad y pregunta si tiene autorización. Usa condiciones para indicar si puede participar según reglas que tú definas y expliques.

### Reto 3 — Calculadora con menú

Solicita dos números y una operación (+, -, *, /). Usa condicionales para realizar la operación elegida. Antes de dividir, comprueba que el segundo número no sea cero.

## 5. Errores frecuentes

- Olvidar los dos puntos después de `if`, `elif` o `else`.
- No indentar el bloque.
- Usar `=` en vez de `==` para comparar.
- Ordenar mal los rangos: una condición amplia al comienzo puede impedir que se alcancen las más específicas.
- Comparar directamente texto de `input()` con números sin convertirlo.

## 6. Cierre

1. ¿Qué diferencia hay entre `if`, `elif` y `else`?
2. ¿Qué hace `and`? ¿Y `or`?
3. ¿Por qué conviene probar los límites de una condición?

## Criterios de logro

- [ ] Escribo condicionales con la indentación correcta.
- [ ] Construyo alternativas con `if`, `elif` y `else`.
- [ ] Combino condiciones sencillas.
- [ ] Pruebo casos normales y casos límite.

## Próxima sesión

**Ciclos:** repetir acciones sin copiar instrucciones una y otra vez.
