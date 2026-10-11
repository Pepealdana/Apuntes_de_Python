# Mapa de posibilidades de Python

Este documento orienta el crecimiento del repositorio. Python no se estudia únicamente para aprender sintaxis: se aprende una base común y luego se exploran distintas áreas de aplicación mediante proyectos pequeños, ejecutables y progresivos.

El objetivo es ampliar las posibilidades tanto del docente como de los estudiantes, sin exigir experiencia profesional, equipos potentes ni licencias de pago.

## Principios de trabajo

- **Primero la lógica, después la biblioteca.** Cada herramienta se introduce cuando resuelve una necesidad concreta.
- **Proyectos pequeños y visibles.** Cada ruta debe permitir construir algo que funcione y se pueda explicar.
- **Bajo consumo de recursos.** Se priorizan herramientas gratuitas y proyectos que puedan ejecutarse en computadores modestos.
- **Instalación gradual.** No se instalan todas las bibliotecas al comienzo.
- **Aprender haciendo.** Cada módulo tendrá conceptos clave, ejemplos ejecutables, retos graduados, errores frecuentes, cierre y una pequeña evidencia de aprendizaje.
- **Separar los proyectos.** Los futuros simuladores educativos de física, química o robótica serán proyectos independientes. No forman parte de las prácticas iniciales de Arduino; más adelante podrán aprovechar conocimientos adquiridos aquí.

## Ruta común: fundamentos

Esta base se reutiliza en todas las áreas.

1. Sintaxis, variables, tipos, operadores, entrada y salida.
2. Condicionales, ciclos y validación.
3. Cadenas y estructuras de datos.
4. Funciones, módulos y organización del código.
5. Errores y excepciones.
6. Archivos, rutas, CSV y JSON.
7. Depuración, pruebas y documentación.
8. Entornos virtuales, instalación de paquetes y uso básico de Git.

No es necesario dominar toda la ruta antes de probar una aplicación pequeña. Los módulos de aplicación pueden volver a los fundamentos cuando los necesiten.

## Campos de aplicación

| Campo | Herramientas posibles | Primeros proyectos educativos |
|---|---|---|
| Programas de consola | Python estándar: `input`, `print`, funciones, `random`, `datetime` | Cuestionarios, conversores, calculadoras, juegos de adivinanza |
| Interfaces gráficas | `tkinter` (incluido con muchas instalaciones de Python), después `CustomTkinter` | Calculadora, formulario, agenda sencilla, panel de seguimiento |
| Juegos 2D | `turtle` para comenzar; después `pygame` | Dibujo interactivo, Pong sencillo, laberinto, juego de preguntas |
| Web y APIs | HTTP y JSON; después `Flask` o `FastAPI`, y `requests` cuando corresponda | Página con datos, API pequeña, consulta de un servicio público |
| Datos y gráficas | `csv`, `json`, `statistics`; después `matplotlib` y, cuando aporte valor, `pandas` | Analizar resultados de una encuesta, comparar mediciones, generar gráficas |
| Automatización | `pathlib`, `shutil`, `csv`, `json`, `openpyxl` si se necesitan archivos Excel | Organizar archivos, generar reportes, procesar listas |
| Imágenes y multimedia | `Pillow` | Redimensionar imágenes, crear miniaturas, convertir formatos |
| Web scraping | `requests` y `BeautifulSoup`, cuando sea apropiado | Extraer datos de páginas públicas respetando sus condiciones de uso |
| Ciencia y cálculo | `math`, `statistics`; después `numpy` si se necesitan arreglos y operaciones numéricas | Explorar funciones, calcular estadísticas, representar datos |
| Inteligencia artificial y aprendizaje automático | Primero conceptos y datos; más adelante bibliotecas específicas según el equipo y el proyecto | Clasificador sencillo con datos pequeños; evaluar límites y resultados |
| Comunicación con dispositivos | `pyserial`, una vez comprendidos archivos, funciones y comunicación básica | Leer datos enviados por un dispositivo y guardarlos en un archivo |
| Calidad y mantenimiento | `unittest` o `pytest`, `logging`, documentación | Probar funciones, registrar errores, mejorar un programa existente |

Las herramientas de cada fila son opciones de una ruta, no una lista de instalaciones obligatorias. Algunas bibliotecas tienen dependencias o requisitos variables; antes de iniciar un módulo se documentarán instalación, compatibilidad y alternativa sin dependencias cuando sea razonable.

## Orden sugerido para incorporar herramientas

### Nivel 1 — Sin bibliotecas externas

- Consola, variables, condicionales, ciclos y funciones.
- Módulos estándar: `random`, `math`, `statistics`, `datetime`, `pathlib`, `csv` y `json`.
- Proyectos pequeños que se ejecuten en cualquier instalación razonable de Python 3.

### Nivel 2 — Interacción visual sencilla

- `turtle` para comprender coordenadas, eventos y secuencias.
- `tkinter` para interfaces básicas.
- `CustomTkinter` para construir interfaces más modernas cuando ya se entiendan funciones, eventos y organización del programa.
- `pygame` para juegos 2D y bucles de actualización.

### Nivel 3 — Datos, archivos y contenido multimedia

- `matplotlib` para gráficas.
- `Pillow` para imágenes.
- `pandas` solo cuando las tablas y operaciones de datos lo justifiquen.
- Lectura y escritura de CSV, JSON y archivos de texto con herramientas estándar.

### Nivel 4 — Web y automatización

- Fundamentos de HTTP, HTML, JSON y APIs.
- `requests` para solicitudes HTTP.
- `Flask` como primera opción ligera para comprender aplicaciones web; `FastAPI` puede venir después para APIs.
- Automatización de archivos y generación de reportes.

### Nivel 5 — Proyectos integradores y exploración

- Pruebas, registros, estructura de proyectos y control de versiones.
- Comunicación con Arduino mediante `pyserial` como una línea de aplicación opcional.
- Proyectos de datos, juegos o web que integren varios conocimientos.
- Exploración introductoria de IA o aprendizaje automático cuando haya una pregunta concreta que resolver.

## Formato de cada módulo

Cada sesión o mini proyecto seguirá, cuando corresponda, esta estructura:

1. **Propósito:** qué se va a construir o comprender.
2. **Conceptos clave:** explicación clara, sin asumir conocimientos no vistos.
3. **Preparación:** programas, bibliotecas e instrucciones de instalación.
4. **Ejemplo guiado:** código completo, ejecutable y comentado.
5. **Prueba y experimentación:** cambiar valores, predecir resultados y observar.
6. **Retos graduados:** básico, intermedio y de ampliación.
7. **Errores frecuentes:** qué ocurre y cómo diagnosticarlo.
8. **Cierre:** preguntas de comprensión y una evidencia breve.
9. **Siguiente paso:** relación con la sesión siguiente o con otro campo de aplicación.
10. **Fuentes:** documentación oficial y materiales externos utilizados.

No todos los módulos necesitan los diez apartados con la misma extensión. La estructura debe ayudar a aprender, no convertirse en una carga.

## Estructura sugerida del repositorio

La organización se aplicará gradualmente, después de revisar y migrar el material existente para conservar su contenido útil.

```text
Apuntes_de_Python/
├── README.md
├── MAPA_DE_POSIBILIDADES.md
├── sesiones/
│   ├── 01-sintaxis-y-variables/
│   ├── 02-operadores/
│   ├── 03-condicionales/
│   └── ...
├── rutas/
│   ├── interfaces-graficas/
│   ├── juegos/
│   ├── web-y-apis/
│   ├── datos-y-graficas/
│   ├── automatizacion/
│   └── imagenes-y-multimedia/
├── proyectos/
│   ├── consola/
│   ├── escritorio/
│   ├── juegos/
│   └── datos/
└── recursos/
    ├── entorno/
    └── referencias/
```

Esta estructura es una propuesta de destino, no una orden para crear todas las carpetas ahora. Primero se revisarán los apuntes actuales; luego se migrarán por etapas, evitando duplicados y pérdida de contenido.

## Cómo elegir el próximo proyecto

Antes de incorporar una biblioteca, el módulo debe responder:

- ¿Qué posibilidad nueva descubre el estudiante?
- ¿Qué conocimientos previos necesita?
- ¿Se puede ejecutar en los equipos disponibles?
- ¿Puede hacerse una versión inicial sin servicios de pago?
- ¿Qué producto concreto queda al terminar?
- ¿Cómo se verifica que funciona?

## Referencias para empezar

- [Documentación oficial de Python en español](https://docs.python.org/es/3/)
- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/)
- [Tkinter — documentación de Python](https://docs.python.org/es/3/library/tkinter.html)
- [CustomTkinter](https://customtkinter.tomschimansky.com/)
- [Pygame](https://www.pygame.org/docs/)
- [Matplotlib](https://matplotlib.org/stable/)
- [Flask](https://flask.palletsprojects.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
