# Apuntes de Python

Repositorio educativo y práctico para aprender Python desde los fundamentos y explorar proyectos pequeños: consola, interfaces gráficas, juegos, web y APIs, automatización, datos, imágenes, ciencia e inteligencia artificial introductoria. Está pensado para aprender y enseñar con herramientas gratuitas y computadores modestos.

## Propósito

El objetivo no es memorizar sintaxis ni instalar todas las bibliotecas al comienzo. Es comprender cómo funciona Python, resolver problemas progresivos y construir proyectos que se puedan explicar, probar y mejorar.

## Cómo trabajar cada sesión

1. Lee el objetivo y los conceptos clave.
2. Ejecuta el ejemplo sin modificarlo.
3. Predice qué ocurrirá antes de cambiar valores.
4. Resuelve los retos sin copiar una solución completa.
5. Revisa los errores frecuentes y prueba una mejora.
6. Explica qué aprendiste y registra las dudas.

Las sesiones incluyen, según el tema, objetivo, conceptos, ejemplo ejecutable, experimentación, retos graduados, diagnóstico de errores, cierre y práctica acumulativa.

## Ruta de aprendizaje

| Etapa | Contenidos |
|---|---|
| 1. Fundamentos | Sintaxis, variables, tipos de datos y comentarios |
| 2. Entrada y salida | `print()`, `input()` y presentación de información |
| 3. Operaciones y lógica | Operadores, práctica integradora y condicionales |
| 4. Repetición y colecciones | Ciclos, cadenas, listas y otras colecciones |
| 5. Organización del código | Funciones, parámetros y valores de retorno |
| 6. Archivos y errores | TXT, CSV, JSON, rutas y excepciones |
| 7. Calidad del código | Depuración, pruebas y documentación |
| 8. Exploración aplicada | Interfaces, juegos, web, automatización, datos, imágenes, ciencia e IA |

No es necesario terminar todas las rutas comunes antes de explorar un campo aplicado. Consulta la [ruta general de aprendizaje](RUTA_GENERAL.md), la [guía del entorno](GUIA_ENTORNO.md), el [mapa de posibilidades](MAPA_DE_POSIBILIDADES.md) y el [catálogo de rutas](rutas/README.md).

## Sesiones de fundamentos

Empieza por el [índice de las sesiones](sesiones/README.md) y avanza en orden:

1. [Sintaxis, variables y tipos](sesiones/01-sintaxis-y-variables/README.md)
2. [Salida con `print()`](sesiones/02-salida-y-print/README.md)
3. [Entrada con `input()`](sesiones/03-entrada-input/README.md)
4. [Operadores](sesiones/04-operadores/README.md)
5. [Práctica integradora](sesiones/05-practica-integradora/README.md)
6. [Condicionales](sesiones/06-condicionales/README.md)
7. [Ciclos](sesiones/07-ciclos/README.md)
8. [Cadenas y colecciones](sesiones/08-cadenas-y-colecciones/README.md)
9. [Funciones](sesiones/09-funciones/README.md)
10. [Archivos y datos](sesiones/10-archivos-y-datos/README.md)
11. [Errores y excepciones](sesiones/11-errores-y-excepciones/README.md)
12. [Mini proyecto de preguntas](sesiones/12-mini-proyecto-preguntas/README.md)

El proyecto acumulativo **Aula organizada** añade una capacidad por sesión sin reemplazar los ejercicios originales. Los apuntes originales de la raíz se conservan como referencia durante la migración.

## Proyectos prácticos

Consulta el [catálogo de proyectos](proyectos/README.md) para conocer cada ejemplo, sus dependencias y cómo ejecutarlo.

- **Interfaces gráficas:** Tkinter, CustomTkinter, calculadora, formulario CSV y gestor JSON.
- **Juegos:** movimiento con Pygame y juego de recolección con colisiones, puntuación, vidas y reinicio.
- **Automatización y datos:** organizador de archivos con simulación predeterminada, reportes CSV y gráficas.
- **Web y APIs:** lista de tareas local con Flask y API REST con GET, POST, PATCH y DELETE.
- **Imágenes:** redimensionamiento proporcional con Pillow.
- **Ciencia:** simulación ideal de proyectil con CSV y gráfica.
- **IA:** clasificador Iris con scikit-learn.

## Pruebas y estado de validación

Las pruebas automatizadas están en [pruebas/README.md](pruebas/README.md). Desde la raíz del repositorio, con las dependencias instaladas, ejecuta:

```bash
python -m compileall -q sesiones proyectos pruebas
python -m unittest discover -s pruebas -v
```

GitHub Actions ejecuta estas comprobaciones con Python 3.12. Las pruebas de humo ejecutan los ejemplos de consola de las 12 sesiones con entradas controladas; otras pruebas cubren lógica, archivos, gráficas, imágenes y rutas Flask/API.

**Importante:** las pruebas automatizadas no sustituyen la validación manual de las ventanas Tkinter/CustomTkinter, la interacción con Pygame ni las comprobaciones desde navegador o cliente HTTP. El estado y las pruebas pendientes están documentados en el [informe de auditoría didáctica y técnica](AUDITORIA_DIDACTICA_Y_TECNICA.md) y el [plan de implementación](PLAN_DE_IMPLEMENTACION.md).

## Preparar el entorno

Se recomienda Python 3.12 para reproducir la configuración de pruebas actual, Visual Studio Code y la extensión oficial de Python. Consulta la [guía de instalación y entornos virtuales](GUIA_ENTORNO.md). Instala solo las dependencias del proyecto que quieras ejecutar; las sesiones iniciales usan la biblioteca estándar.

## Licencias

- **Apuntes, explicaciones, ejercicios y documentación original:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), descrita en [LICENSE](LICENSE).
- **Código fuente de ejemplo:** licencia MIT, descrita en [LICENSE-CODE](LICENSE-CODE).
- **Contenido de terceros:** conserva su licencia original; verifica sus condiciones antes de reutilizarlo.

La licencia solo cubre materiales sobre los que se tienen derechos suficientes. Al reutilizar material, atribuye la autoría y señala los cambios.

## Referencias iniciales

- [Documentación oficial de Python en español](https://docs.python.org/es/3/)
- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/)
- [Tkinter](https://docs.python.org/es/3/library/tkinter.html)
- [CustomTkinter](https://customtkinter.tomschimansky.com/)
- [Pygame](https://www.pygame.org/docs/)
- [Matplotlib](https://matplotlib.org/stable/)
- [Flask](https://flask.palletsprojects.com/)
- [scikit-learn](https://scikit-learn.org/stable/)

## Autoría y adaptación

Material educativo elaborado y adaptado progresivamente por Peters Aldana. Las fuentes externas y los materiales de terceros deben atribuirse según corresponda.
