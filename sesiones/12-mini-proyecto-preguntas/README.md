# Sesión 12. Mini proyecto: concurso de preguntas

**Nivel:** inicial-intermedio  
**Requisitos previos:** sesiones 1 a 11  
**Herramientas:** Python 3, sin bibliotecas externas  
**Producto:** un concurso de preguntas en consola con puntuación y resumen.

## Objetivo

Integrar variables, listas, diccionarios, funciones, ciclos, condicionales y validación en un programa pequeño y completo.

## 1. Qué construirás

El programa presenta preguntas de selección múltiple, recibe una respuesta, comprueba si es correcta, suma puntos y muestra un resumen final.

Este proyecto no busca ser un juego avanzado. Busca demostrar que los fundamentos permiten construir algo funcional sin instalar bibliotecas.

## 2. Ejecuta el ejemplo

Abre [12_concurso_preguntas.py](ejemplos/12_concurso_preguntas.py) y ejecútalo. El archivo contiene las preguntas y la lógica del concurso.

## 3. Analiza la estructura

- Una lista almacena las preguntas.
- Cada pregunta es un diccionario con enunciado, opciones y respuesta correcta.
- Una función presenta la pregunta.
- Un ciclo recorre las preguntas.
- Una condición compara la respuesta.
- Una variable acumuladora conserva la puntuación.
- El resultado final resume los aciertos.

## 4. Retos de ampliación

### Reto 1 — Crear preguntas

Añade dos preguntas de tecnología, ciencias, matemáticas o cultura general. Comprueba que las respuestas sean correctas.

### Reto 2 — Respuestas sin distinguir mayúsculas

Permite escribir `a`, `A`, `b` o `B` usando `strip().upper()`.

### Reto 3 — Mostrar porcentaje

Calcula el porcentaje de aciertos. Evita dividir entre cero si no hay preguntas.

### Reto 4 — Guardar resultados

Guarda la puntuación final en un archivo de texto. Reutiliza la sesión 10.

### Reto 5 — Elegir categoría

Añade una categoría a cada pregunta y permite filtrar las preguntas que se presentan.

## 5. Criterios de logro

- [ ] El programa presenta las preguntas.
- [ ] Acepta respuestas y valida opciones.
- [ ] Calcula correctamente la puntuación.
- [ ] Muestra un resumen final.
- [ ] Puedo explicar dónde se usan listas, diccionarios, funciones, ciclos y condicionales.

## 6. Cierre

Explica qué parte fue más sencilla, cuál requirió más depuración y qué cambiarías para que el concurso fuera más útil para tus estudiantes.

## Próximas rutas

Después de este proyecto, el repositorio podrá abrir rutas aplicadas: interfaces gráficas, juegos 2D, automatización, visualización de datos y web. Cada ruta reutilizará estos fundamentos.


## Práctica acumulativa — Proyecto final: Aula organizada

Como alternativa o extensión al concurso, integra el proyecto acumulativo en una pequeña aplicación de consola: registra actividades, calcula presupuestos, valida entradas, permite consultar el listado y guarda los datos en JSON. Divide la lógica en funciones.

**Criterio de revisión:** el flujo principal funciona, los datos persisten entre ejecuciones, se validan las entradas y las funciones tienen responsabilidades claras.

**Evidencia:** realiza una prueba completa con datos ficticios, muestra el archivo JSON generado y escribe tres mejoras posibles. El concurso de preguntas original se conserva como proyecto integrador de esta sesión.
