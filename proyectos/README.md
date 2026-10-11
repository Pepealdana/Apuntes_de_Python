# Proyectos prácticos

Los proyectos de esta carpeta permiten explorar distintas aplicaciones de Python. Ejecuta primero el ejemplo, después modifica sus datos y finalmente resuelve un reto. Las instrucciones de cada proyecto indican qué instalar y desde qué carpeta ejecutar los comandos.

## Interfaces gráficas

| Proyecto | Requisito | Qué permite practicar |
|---|---|---|
| [Tkinter: primera ventana](interfaces/tkinter_primera_ventana.py) | Python con Tkinter | Ventana, etiqueta, botón y eventos |
| [CustomTkinter: primera aplicación](interfaces/customtkinter_inicio.py) | `customtkinter` | Ventana y respuesta a eventos |
| [Calculadora](interfaces/calculadora_customtkinter.py) | `customtkinter` | Operaciones, validación y división por cero |
| [Formulario](interfaces/formulario_estudiantes.py) | `customtkinter` | Campos obligatorios y almacenamiento CSV |
| [Gestor de actividades](interfaces/gestor_actividades_json.py) | `customtkinter` | Altas, consulta, eliminación y persistencia JSON |
| [Guía de interfaces](interfaces/README.md) | — | Preparación, secuencia y retos |

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
| [Organizador de archivos](automatizacion/organizar_archivos.py) | Python estándar | Rutas y simulación antes de mover |
| [Informe de mediciones](datos/reporte_mediciones.py) | Python estándar | Validación CSV y generación de informe |
| [Gráfica de mediciones](datos/grafica_datos.py) | `matplotlib` | Graficar series desde CSV |
| [Datos de prueba](datos/mediciones_prueba.csv) | — | Registros ficticios, incluidas filas inválidas |

## Web, imágenes, ciencia e IA

| Proyecto | Requisito | Qué permite practicar |
|---|---|---|
| [Lista de tareas web](web/app_tareas_flask.py) | `flask` | Rutas, formularios, validación y JSON |
| [API REST de tareas](web/api_tareas.py) | `flask` | GET, POST, PATCH, DELETE y JSON ([guía](web/api_tareas_README.md)) |
| [Redimensionar imágenes](imagenes/redimensionar_imagen.py) | `pillow` | Proporciones, formatos y copias seguras |
| [Simulación de proyectil](ciencia/simulacion_proyectil.py) | `matplotlib` | Modelo matemático, CSV y gráfica |
| [Clasificador Iris](ia/clasificador_iris.py) | `scikit-learn` | Entrenamiento, prueba y métricas |

## Preparación y ejecución

1. Abre la carpeta del repositorio en Visual Studio Code.
2. Consulta la [guía de entorno virtual e instalación](../GUIA_ENTORNO.md).
3. Crea un entorno virtual e instala solo las dependencias necesarias.
4. Ejecuta los comandos desde la raíz del repositorio cuando así se indique.
5. Cambia un valor, predice el resultado y vuelve a ejecutar.
6. Resuelve al menos un reto antes de pasar al siguiente proyecto.

Los archivos CSV/JSON y otros resultados suelen crearse en el directorio de trabajo actual, no necesariamente junto al script. Lee el encabezado y el README de cada proyecto antes de ejecutarlo.

## Seguridad y estado de validación

El organizador de archivos funciona en modo simulación por defecto; usa `--aplicar` solo después de revisar el plan y probar en una carpeta temporal. Las aplicaciones Flask y la API son demostraciones locales: no las expongas a internet ni introduzcas datos sensibles.

La compilación y las pruebas automatizadas cubren los casos documentados, pero no equivalen a una prueba visual de interfaces o juegos ni a una prueba manual desde navegador. Consulta el [informe de auditoría](../AUDITORIA_DIDACTICA_Y_TECNICA.md).
