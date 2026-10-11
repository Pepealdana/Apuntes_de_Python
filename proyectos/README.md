# Proyectos prácticos

Los proyectos de esta carpeta son puntos de partida ejecutables para experimentar con distintas aplicaciones de Python. Primero se ejecuta el ejemplo, después se modifica y finalmente se amplía.

## Interfaces gráficas

| Proyecto | Requisito | Qué permite practicar |
|---|---|---|
| [Tkinter: primera ventana](interfaces/tkinter_primera_ventana.py) | Python con Tkinter | Ventana, etiqueta, botón y eventos |
| [CustomTkinter: primera aplicación](interfaces/customtkinter_inicio.py) | `customtkinter` | Ventana moderna y respuesta a eventos |
| [Calculadora](interfaces/calculadora_customtkinter.py) | `customtkinter` | Operaciones, validación y división por cero |
| [Formulario](interfaces/formulario_estudiantes.py) | `customtkinter` | Campos obligatorios y almacenamiento CSV |
| [Gestor de actividades](interfaces/gestor_actividades_json.py) | `customtkinter` | Altas, consulta, eliminación y persistencia JSON |
| [Guía de interfaces](interfaces/README.md) | — | Instrucciones, secuencia y retos |

## Juegos

| Proyecto | Requisito | Qué permite practicar |
|---|---|---|
| [Mover un objeto](juegos/pygame_mover_objeto.py) | `pygame` | Eventos, coordenadas y bucle principal |
| [Recolecta las estrellas](juegos/pygame_recolectar.py) | `pygame` | Colisiones, puntuación, vidas, victoria y reinicio |
| [Guía de juegos](juegos/README.md) | — | Preparación, controles y retos |

## Automatización y datos

| Proyecto | Requisito | Qué permite practicar |
|---|---|---|
| [Reporte CSV básico](automatizacion/reporte_csv.py) | Python estándar | Lectura, validación y resumen |
| [Organizador de archivos](automatizacion/organizar_archivos.py) | Python estándar | Rutas y modo de simulación antes de mover |
| [Informe de mediciones](datos/reporte_mediciones.py) | Python estándar | Validación de CSV y generación de informe |
| [Gráfica de mediciones](datos/grafica_datos.py) | `matplotlib` | Graficar series desde un CSV |
| [Datos de prueba](datos/mediciones_prueba.csv) | — | Registros ficticios, incluidas filas inválidas |

## Web, imágenes, ciencia e IA

| Proyecto | Requisito | Qué permite practicar |
|---|---|---|
| [Lista de tareas web](web/app_tareas_flask.py) | `flask` | Rutas, formularios, validación y JSON |\n| [API REST de tareas](web/api_tareas.py) | `flask` | GET, POST, PATCH, DELETE y respuestas JSON |
| [Redimensionar imágenes](imagenes/redimensionar_imagen.py) | `pillow` | Proporciones, formatos y copias seguras |
| [Simulación de proyectil](ciencia/simulacion_proyectil.py) | `matplotlib` | Modelo matemático, CSV y gráfica |
| [Clasificador Iris](ia/clasificador_iris.py) | `scikit-learn` | Entrenamiento, prueba y métricas |

## Preparación del entorno

Antes de instalar bibliotecas externas, sigue la [guía de entorno virtual e instalación](../GUIA_ENTORNO.md). Instala únicamente las dependencias del proyecto que vayas a ejecutar.

## Cómo ejecutar

1. Abre la carpeta del repositorio en Visual Studio Code.
2. Revisa el README de la subcarpeta y sus dependencias.
3. Crea un entorno virtual e instala solo los paquetes necesarios.
4. Ejecuta los comandos desde la raíz del repositorio cuando así se indique.
5. Cambia un valor, predice el resultado y vuelve a ejecutar.
6. Resuelve al menos un reto antes de pasar al siguiente proyecto.

Los ejemplos son material didáctico y no implican que hayan sido probados en todos los sistemas operativos. La sintaxis se comprueba con GitHub Actions; la ejecución de interfaces, juegos, servidores web y generación de archivos requiere pruebas adicionales.
