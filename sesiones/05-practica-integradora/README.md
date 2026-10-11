# Sesión 5. Práctica integradora: la historia del oso

**Nivel:** inicial  
**Requisitos previos:** sesiones 1 a 4  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto:** un programa que calcula distancias y presenta una historia.

## Objetivo

Integrar variables, tipos de datos, operadores, entrada opcional y salida legible en un programa pequeño.

## 1. Situación

Un oso recorre 26 km hacia el sur, luego 19 km hacia el este y finalmente 57 km hacia el norte.

El programa debe calcular la distancia total recorrida. No debe confundir la distancia total con el desplazamiento geográfico: para este ejercicio solo sumaremos los kilómetros caminados.

## 2. Ejemplo guiado

Ejecuta [05_historia_del_oso.py](ejemplos/05_historia_del_oso.py). Identifica dónde se guardan las distancias, dónde se calcula el total y cómo se presenta el resultado. Para comprobar el reto de las monedas, consulta [05_compra_chocolates.py](ejemplos/05_compra_chocolates.py), que separa el cálculo del dinero disponible, la cantidad de chocolates completos y el sobrante.

El total correcto es 26 + 19 + 57 = 102 km.

En los apuntes originales, la variable `suma` se incrementaba en 20 antes de presentar la historia, por lo que el total mostrado terminaba siendo 122 km. En la nueva versión se conserva `distancia_total` y se usa otra variable para las operaciones adicionales.

## 3. Experimenta

1. Cambia las tres distancias y comprueba el total.
2. Añade una variable para el nombre del animal.
3. Calcula cuánto recorrió en los dos primeros tramos.
4. Compara la distancia del primer tramo con la del segundo.
5. Cambia el título sin modificar los cálculos.

## 4. Retos

### Reto 1 — Historia propia

Crea una historia de tres recorridos con un animal, un robot o un personaje. Guarda distancias y direcciones en variables.

### Reto 2 — Compra de chocolates

Una persona tiene 12 monedas, presta 9, paga una deuda de 2 y encuentra 7. Cada chocolate cuesta 2 monedas.

Calcula:
- Las monedas disponibles al final.
- Cuántos chocolates completos puede comprar.
- Cuántas monedas sobran.

No uses una sola variable para representar cantidades diferentes.

### Reto 3 — Personalización

Solicita por teclado el nombre del personaje y muestra la historia con ese nombre. Si lo necesitas, vuelve a consultar la sesión de entrada con `input()`.

## Errores frecuentes y diagnóstico

- **Los valores no se incorporan a la historia:** revisa si estás usando la variable o escribiendo su nombre como texto.
- **El cálculo no coincide con la predicción:** verifica el orden de las operaciones y los valores de entrada.
- **La salida es difícil de leer:** separa el cálculo de la presentación y usa cadenas f.
- **El programa falla al ejecutar:** lee la última línea del mensaje de error y comprueba primero la sintaxis y los nombres de variables.

## 5. Cierre

- ¿Qué bug se produjo al modificar la variable del total?
- ¿Por qué es útil elegir nombres descriptivos?
- ¿Qué conceptos de las sesiones anteriores usaste?

## Criterios de logro

- [ ] Declaro variables con nombres comprensibles.
- [ ] Calculo correctamente la suma de distancias.
- [ ] Presento resultados con `print()`.
- [ ] Distingo el total original de los cálculos auxiliares.
- [ ] Puedo explicar qué hace cada parte del programa.

## Siguiente paso

Continuar con condicionales para que el programa tome decisiones a partir de los datos.


## Práctica acumulativa — Proyecto: Aula organizada

Integra las sesiones 1–4 en un solo programa: pide la actividad, el área, la cantidad y el costo unitario; calcula el total y muestra una ficha final. Mantén el ejercicio original de la historia del oso: esta actividad acumulativa es adicional, no lo reemplaza.

**Criterio de revisión:** los datos se solicitan una vez, los cálculos usan las variables y el resultado es fácil de leer.

**Evidencia:** explica en qué parte se utilizan variables, entrada, salida y operadores.
