# Auditoría didáctica, documental y técnica

**Repositorio:** [Apuntes_de_Python](https://github.com/Pepealdana/Apuntes_de_Python)  
**Revisión:** octubre de 2026  
**Alcance:** sesiones 1–12, ejemplos de consola, proyectos aplicados, pruebas automatizadas, instrucciones y licencias.

## Cómo interpretar el estado

- **Revisado:** se inspeccionó el código o la documentación y se comprobó su coherencia mediante lectura estática.
- **Prueba automatizada:** una prueba ejecuta la lógica o el flujo indicado dentro del entorno de pruebas.
- **Pendiente de escritorio:** requiere abrir una ventana, interactuar con teclado/ratón o comprobar la presentación en un equipo real.
- **Pendiente local:** requiere ejecutar el servidor y verificarlo desde un navegador o cliente HTTP fuera del cliente de pruebas de Flask.

No se declara que una interfaz haya sido validada visualmente si no se ha abierto en un escritorio real. GitHub Actions terminó correctamente en la ejecución [#47](https://github.com/Pepealdana/Apuntes_de_Python/actions/runs/38158313719): compilación de sintaxis correcta y 30 pruebas automatizadas aprobadas, incluida la comprobación de enlaces internos y la ejecución de los 13 ejemplos de las sesiones.

## 1. Auditoría didáctica de las sesiones

| Sesión | Tema | Coherencia revisada | Evidencia de ejecución |
|---|---|---|---|
| 1 | Sintaxis, variables y tipos | Los conceptos y retos corresponden al ejemplo; se distingue texto, entero, decimal y booleano. | Prueba de humo automatizada |
| 2 | Salida con `print()` | El ejemplo demuestra argumentos, cadenas, saltos de línea y `end`. | Prueba de humo automatizada |
| 3 | Entrada con `input()` | Se explica que la entrada es texto y se convierte la edad a entero; la prueba suministra entradas válidas. | Prueba de humo automatizada |
| 4 | Operadores | Se ilustran aritmética, precedencia, comparación, asignación, identidad y pertenencia. | Prueba de humo automatizada |
| 5 | Práctica integradora | Los ejemplos combinan variables, cálculos y salida; el problema de monedas distingue división entera y residuo. | Ambos ejemplos en pruebas de humo |
| 6 | Condicionales | Las funciones y ramas `if/elif/else` cubren rangos de temperatura, nota y condición compuesta. | Prueba de humo automatizada |
| 7 | Ciclos | Los ejemplos muestran `for`, `range`, acumulación y un `while` con avance del contador. | Prueba de humo automatizada |
| 8 | Cadenas y colecciones | Se muestran limpieza de texto, índices, longitud, listas, pertenencia y conteo de vocales. | Prueba de humo automatizada |
| 9 | Funciones | Los ejemplos usan parámetros y `return` con operaciones sencillas. | Prueba de humo automatizada |
| 10 | Archivos y datos | Se crean TXT, CSV y JSON usando rutas relativas y codificación UTF-8; se leen datos guardados. | Prueba de humo automatizada |
| 11 | Errores y excepciones | Se manejan entradas no enteras y no numéricas y se evita dividir entre cero. | Prueba de humo automatizada con entradas válidas |
| 12 | Concurso de preguntas | El bucle valida A/B/C, acumula aciertos y calcula porcentaje; también contempla una lista vacía en la función de cálculo. | Prueba de humo automatizada |

Las sesiones mantienen el orden real de aprendizaje: sintaxis y variables, salida, entrada, operadores, práctica integradora, condicionales, ciclos, cadenas y colecciones, funciones, archivos, excepciones y cuestionario. La práctica «Aula organizada» complementa los ejercicios originales.

## 2. Auditoría de proyectos

| Proyecto | Lógica revisada / prueba automatizada | Pendiente práctico |
|---|---|---|
| Organizador de archivos | Planificación, simulación predeterminada y prevención de sobrescritura; pruebas de planificación. | Probar `--aplicar` con una carpeta temporal en Windows. |
| Reporte CSV básico | Lectura de columna requerida, omisión de puntajes inválidos y cálculo de resumen; se agregaron pruebas. | Verificar mensajes en terminal con archivos preparados por el usuario. |
| Informe de mediciones | Validación de columnas, campos vacíos, valores numéricos finitos y salidas CSV/TXT; pruebas de lectura y generación. | Revisar visualmente el informe generado con datos propios ficticios. |
| Gráfica de mediciones | Lectura de CSV, omisión de filas inválidas y exportación PNG; se rechazan NaN e infinito. | Abrir la gráfica en escritorio y comprobar etiquetas con datos largos. |
| Calculadora CustomTkinter | Operaciones separadas de la interfaz, división por cero, operación desconocida y números no finitos; pruebas de lógica. | Abrir la ventana y probar campos vacíos, coma decimal y botones. |
| Formulario CustomTkinter | Validación de campos y persistencia CSV con encabezado único; prueba de escritura. | Probar el formulario y errores de permisos en Windows. |
| Gestor JSON CustomTkinter | Carga, escritura atómica, estructura inicial inválida, altas y eliminación con confirmación; prueba de persistencia. | Abrir la ventana, probar selección y recuperación manual de un JSON dañado. |
| Ventana Tkinter / inicio CustomTkinter | Eventos y respuesta de controles revisados por lectura de código. | Comprobar dimensiones, fuentes y comportamiento en pantalla pequeña. |
| Movimiento Pygame | Bucle de eventos, delta de tiempo y límites de pantalla revisados. | Probar teclado, movimiento y cierre de ventana. |
| Recolecta las estrellas | Estado inicial, distribución de elementos, puntuación, vidas, colisiones, victoria y reinicio revisados; prueba de estado inicial. | Jugar varias partidas y comprobar colisiones, dificultad y reinicio. |
| Flask: lista de tareas | Rutas CRUD, validación de título y persistencia JSON; pruebas con cliente de Flask. | Ejecutar servidor y probar desde un navegador local. |
| API REST de tareas | GET/POST/PATCH/DELETE, validación de payload e identificadores y persistencia; pruebas con cliente de Flask. | Ejecutar servidor y repetir solicitudes con `curl`. |
| Redimensionamiento Pillow | Proporción, orientación EXIF, copia de salida y prevención de sobrescritura; pruebas con imágenes generadas. | Probar imágenes reales JPG/PNG de varias orientaciones y modos de color. |
| Simulación de proyectil | Modelo ideal, validación de parámetros finitos, CSV y gráfica; prueba de exportación. | Comparar cálculos con una segunda fuente y revisar PNG en escritorio. |
| Clasificador Iris | Separación entrenamiento/prueba, escalado, regresión logística y métricas; prueba de ejecución y reporte. | Interpretar la matriz de confusión y explicar el resultado al grupo. |

## 3. Correcciones incorporadas en esta auditoría

- Se separó la lógica matemática de la calculadora de su interfaz para poder probar las cuatro operaciones sin abrir una ventana.
- Se añadieron validaciones para rechazar `NaN`, infinito y parámetros no finitos en la calculadora, el simulador de proyectil y los procesadores de mediciones CSV.
- Se añadieron pruebas de humo para ejecutar los 13 ejemplos Python de las sesiones 1–12 con entradas controladas.
- Se ampliaron las pruebas de CSV, calculadora, formulario y parámetros científicos.
- Se añadieron avisos de licencia separados para el material educativo y el código fuente.
- Se corrigieron las instrucciones del README principal y el catálogo de proyectos; se añadió una prueba automatizada para detectar enlaces internos Markdown rotos.

## 4. Licencias

- **Material educativo original** — explicaciones, apuntes, guías, ejercicios y documentación: [Creative Commons Atribución 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Permite reutilización y adaptación, incluso comercial, con atribución.
- **Código fuente de ejemplo** — archivos Python del repositorio: licencia MIT, descrita en [LICENSE-CODE](LICENSE-CODE).
- **Material de terceros** — conserva la licencia que le corresponda; no se debe relicenciar sin permiso.

La licencia se aplica solo a materiales sobre los que el autor tiene derechos suficientes. Si se incorporan obras externas, se debe comprobar y documentar su licencia.

## 5. Qué significa que los proyectos estén validados

La compilación de sintaxis y las pruebas automatizadas demuestran únicamente los casos que ejecutan. No reemplazan las pruebas de escritorio, el uso real del servidor ni la revisión visual de archivos generados. Antes de declarar la versión estable para uso educativo, hay que completar la lista de pruebas manuales en Windows y actualizar este informe con sus resultados.

## 6. Lista de comprobación manual en Windows

- [ ] Activar un entorno virtual limpio e instalar las dependencias de cada proyecto.
- [ ] Abrir y probar calculadora, formulario, gestor JSON, Tkinter inicial y CustomTkinter inicial.
- [ ] Probar el juego Pygame: teclado, límites, colisiones, vidas, victoria, reinicio y cierre.
- [ ] Ejecutar organizador en simulación y luego con `--aplicar` únicamente en una carpeta temporal.
- [ ] Ejecutar los reportes y revisar CSV/TXT/PNG generados.
- [ ] Probar Flask en navegador y API con `curl`.
- [ ] Probar Pillow con JPG y PNG, incluida una imagen con orientación EXIF.
- [ ] Revisar salida del clasificador Iris y explicar la matriz de confusión.
- [ ] Confirmar GitHub Actions en la rama de esta auditoría.
