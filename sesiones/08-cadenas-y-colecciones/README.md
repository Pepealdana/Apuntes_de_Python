# Sesión 8. Cadenas y colecciones básicas

**Nivel:** inicial  
**Requisitos previos:** sesiones 1 a 7  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto:** un programa que procesa texto y trabaja con listas.

## Objetivo

Explorar operaciones básicas de cadenas y aprender a crear, consultar y recorrer listas.

## 1. Conceptos clave

### Cadenas de texto (`str`)

Una cadena contiene texto. Las posiciones empiezan en cero:

```python
palabra = "Python"
print(palabra[0])   # P
print(palabra[-1])  # n
print(len(palabra)) # 6
```

Una cadena es inmutable: no se modifica un carácter directamente. Se puede crear otra cadena a partir de ella.

```python
nombre = "  ana  "
nombre_limpio = nombre.strip().title()
print(nombre_limpio)  # Ana
```

Métodos útiles:
- `strip()`: quita espacios al comienzo y al final.
- `lower()`: convierte a minúsculas.
- `upper()`: convierte a mayúsculas.
- `title()`: pone en mayúscula inicial las palabras.
- `replace(viejo, nuevo)`: crea una cadena con reemplazos.
- `split()`: divide el texto en una lista.

### Listas

Una lista guarda varios elementos y se escribe entre corchetes. Es ordenada y modificable.

```python
materiales = ["LED", "resistencia", "cable"]
print(materiales[0])
materiales.append("protoboard")
print(len(materiales))
```

Índices comienzan en cero. Un índice inexistente provoca `IndexError`.

Operaciones iniciales:
- `append(elemento)`: añade un elemento al final.
- `remove(elemento)`: elimina la primera coincidencia.
- `len(lista)`: cuenta elementos.
- `elemento in lista`: comprueba pertenencia.

### Recorrer una lista

```python
for material in materiales:
    print(material)
```

### Tuplas, diccionarios y conjuntos: primera mirada

- **Tupla (`tuple`):** colección ordenada que no se modifica normalmente después de crearla: `coordenada = (3, 5)`.
- **Diccionario (`dict`):** relaciona claves y valores: `estudiante = {"nombre": "Ana", "edad": 15}`.
- **Conjunto (`set`):** guarda elementos únicos: `colores = {"azul", "rojo"}`.

En esta sesión se profundiza en cadenas y listas. Los diccionarios y conjuntos se retomarán con más ejemplos cuando se necesiten para proyectos.

## 2. Ejemplo guiado

Ejecuta [08_cadenas_y_listas.py](ejemplos/08_cadenas_y_listas.py).

## 3. Experimenta

1. Cambia la palabra y prueba índices positivos y negativos.
2. Limpia un nombre con espacios usando `strip()`.
3. Añade y elimina elementos de la lista.
4. Comprueba con `in` si un material está presente.
5. Recorre una lista e imprime cada elemento.

## 4. Retos

### Reto 1 — Limpiador de nombres

Pide un nombre y apellido, elimina espacios sobrantes y muestra el nombre con formato de título.

### Reto 2 — Lista de materiales

Crea una lista de cinco materiales para una actividad escolar. Añade uno, elimina otro y muestra la lista final.

### Reto 3 — Conteo de vocales

Recorre una palabra convertida a minúsculas y cuenta cuántas letras son vocales. No necesitas una biblioteca externa.

## 5. Errores frecuentes

- Olvidar que el primer índice es cero.
- Intentar cambiar un carácter de una cadena directamente.
- Confundir `append()` con `extend()` (se estudiará después).
- Llamar a un método sin paréntesis.
- Suponer que los conjuntos conservan el orden de una lista.

## 6. Cierre

1. ¿Qué diferencia hay entre una cadena y una lista?
2. ¿Qué hace `len()`?
3. ¿Cómo recorres todos los elementos de una lista?
4. ¿En qué caso usarías una tupla o un diccionario?

## Criterios de logro

- [ ] Consulto caracteres e índices de una cadena.
- [ ] Uso métodos básicos de texto.
- [ ] Creo y modifico listas.
- [ ] Recorro colecciones con `for`.
- [ ] Distingo listas, tuplas, diccionarios y conjuntos.

## Próxima sesión

**Funciones:** organizar instrucciones reutilizables.
