# Apuntes de Python

Repositorio educativo y práctico para aprender Python desde los fundamentos y explorar, paso a paso, distintas cosas que se pueden construir con el lenguaje. Está pensado para aprender y enseñar con proyectos pequeños, herramientas gratuitas y computadores modestos.

## Propósito

No queremos aprender únicamente sintaxis. Queremos entender cómo funciona Python y descubrir sus campos de aplicación: programas de consola, interfaces gráficas, juegos, web y APIs, automatización, datos, imágenes, ciencia y comunicación con dispositivos.

El objetivo no es abarcar todas las bibliotecas ni formar profesionales en una sola ruta. Es construir fundamentos transferibles, explorar posibilidades y desarrollar proyectos que puedan explicarse, probarse y mejorarse.

## Cómo trabajar cada sesión

1. Lee los conceptos clave.
2. Ejecuta el ejemplo sin modificarlo.
3. Cambia algunos valores y predice qué ocurrirá.
4. Resuelve los retos sin copiar la solución.
5. Revisa los errores frecuentes y prueba una mejora.
6. Registra qué aprendiste y qué dudas quedan.

Cada módulo tendrá, según lo que necesite, propósito, conceptos, preparación, ejemplo ejecutable, experimentación, retos graduados, errores frecuentes, cierre y fuentes.

## Ruta de aprendizaje

| Etapa | Contenidos |
|---|---|
| 1. Fundamentos | Sintaxis, variables, tipos, operadores, entrada y salida |
| 2. Control de flujo | Condicionales, ciclos y validación |
| 3. Estructuras de datos | Cadenas, listas, tuplas, diccionarios y conjuntos |
| 4. Funciones y módulos | Funciones, alcance, módulos y organización |
| 5. Archivos y errores | Excepciones, archivos, CSV, JSON y rutas |
| 6. Calidad del código | Depuración, pruebas, registros y documentación |
| 7. Exploración aplicada | Interfaces, juegos, web, automatización, datos, imágenes y ciencia |
| 8. Proyectos integradores | Aplicaciones pequeñas que combinan conocimientos de distintas etapas |

No es necesario terminar toda la ruta común antes de explorar un campo de aplicación. Los proyectos volverán a los fundamentos cuando lo necesiten.

Consulta la [ruta general de aprendizaje](RUTA_GENERAL.md) para ver las etapas y la secuencia recomendada. Antes de instalar bibliotecas externas, revisa la [guía de entorno virtual e instalación](GUIA_ENTORNO.md).

## Campos de aplicación

- **Consola y lógica:** calculadoras, cuestionarios, conversores y juegos de texto.
- **Interfaces gráficas:** Tkinter y CustomTkinter.
- **Juegos:** Turtle para comenzar y Pygame para juegos 2D.
- **Web y APIs:** fundamentos de HTTP, JSON, Flask y FastAPI.
- **Datos y gráficas:** módulos estándar, Matplotlib y, cuando aporte valor, pandas.
- **Automatización:** organización de archivos, procesamiento de información y generación de reportes.
- **Imágenes y multimedia:** Pillow y proyectos sencillos de edición de imágenes.
- **Ciencia y cálculo:** matemáticas, estadísticas y visualización de fenómenos.
- **Inteligencia artificial:** exploración introductoria cuando exista un problema concreto y el equipo lo permita.
- **Dispositivos:** comunicación serial con Arduino como una posibilidad adicional, no como el centro del repositorio.

La incorporación de bibliotecas será gradual: no se instalarán todas al comienzo. Se priorizarán herramientas gratuitas y ejemplos que puedan ejecutarse en equipos modestos.

Consulta el [Mapa de posibilidades de Python](MAPA_DE_POSIBILIDADES.md) para ver las herramientas previstas y el [catálogo de rutas](rutas/README.md) para comenzar un área aplicada.

## Sesiones de fundamentos

Consulta el [índice de sesiones](sesiones/README.md) para seguir la ruta en orden.

- [Sesión 1: Sintaxis, variables y tipos de datos](sesiones/01-sintaxis-y-variables/README.md)
- [Sesión 2: Mostrar información con print()](sesiones/02-salida-y-print/README.md)
- [Sesión 3: Recibir información con input()](sesiones/03-entrada-input/README.md)
- [Sesión 4: Operadores](sesiones/04-operadores/README.md)
- [Sesión 5: Práctica integradora](sesiones/05-practica-integradora/README.md)
- [Sesión 6: Condicionales](sesiones/06-condicionales/README.md)
- [Sesión 7: Ciclos](sesiones/07-ciclos/README.md)
- [Sesión 8: Cadenas y colecciones](sesiones/08-cadenas-y-colecciones/README.md)
- [Sesión 9: Funciones](sesiones/09-funciones/README.md)
- [Sesión 10: Archivos y datos](sesiones/10-archivos-y-datos/README.md)
- [Sesión 11: Errores y excepciones](sesiones/11-errores-y-excepciones/README.md)
- [Sesión 12: Mini proyecto de preguntas](sesiones/12-mini-proyecto-preguntas/README.md)

## Proyectos prácticos

El repositorio ahora incluye proyectos iniciales y versiones más completas en varias áreas. Consulta el [catálogo de proyectos](proyectos/README.md) para ver dependencias, instrucciones y retos.

- **Interfaces:** calculadora con CustomTkinter, formulario con CSV y gestor de actividades con JSON.
- **Juegos:** movimiento inicial y juego de recolección con colisiones, puntuación, vidas y reinicio mediante Pygame.
- **Automatización y datos:** organizador de archivos con modo simulación, informe CSV validado y gráfica de mediciones.
- **Web:** lista de tareas local con Flask y persistencia JSON.
- **Imágenes:** redimensionamiento de copias con Pillow.
- **Ciencia:** simulación ideal de proyectil con CSV y gráfica.
- **IA:** experimento de clasificación Iris con scikit-learn.

Los proyectos están incorporados en el repositorio, pero no todos han sido ejecutados en un entorno gráfico real. El plan de implementación diferencia explícitamente el código disponible de las pruebas que faltan.

## Entorno recomendado

- Python 3
- Visual Studio Code
- Extensión oficial de Python para VS Code

Las sesiones iniciales no requieren bibliotecas externas. Cada nueva herramienta tendrá instrucciones de instalación y un ejemplo pequeño antes de convertirse en requisito. GitHub Actions comprueba la sintaxis de los scripts Python incluidos en las carpetas de sesiones y proyectos; esa comprobación no sustituye las pruebas de ejecución.

## Seguimiento

Consulta el [plan de implementación](PLAN_DE_IMPLEMENTACION.md) para distinguir lo incorporado de lo pendiente de probar y ampliar.

## Referencias iniciales

- [Documentación oficial de Python en español](https://docs.python.org/es/3/)
- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/)
- [Tkinter — documentación de Python](https://docs.python.org/es/3/library/tkinter.html)
- [CustomTkinter](https://customtkinter.tomschimansky.com/)
- [Pygame](https://www.pygame.org/docs/)
- [Matplotlib](https://matplotlib.org/stable/)
- [Flask](https://flask.palletsprojects.com/)
- [FastAPI](https://fastapi.tiangolo.com/)

## Autoría y adaptación

Material de aprendizaje elaborado y adaptado progresivamente por Peters Aldana. Cuando se reutilicen ideas o materiales de terceros, se procurará indicar la fuente correspondiente.
