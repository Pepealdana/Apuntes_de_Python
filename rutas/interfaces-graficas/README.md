# Ruta: interfaces gráficas de escritorio

## Propósito

Aprender a convertir programas de consola en aplicaciones con ventanas, botones, campos de entrada y mensajes. La progresión va de herramientas incluidas con Python a una biblioteca de apariencia moderna.

## Secuencia recomendada

1. **Turtle:** coordenadas, dibujo, eventos y experimentación visual.
2. **Tkinter:** ventanas, etiquetas, botones, campos, disposición y eventos.
3. **Funciones y eventos:** separar la lógica del programa de las acciones de la interfaz.
4. **CustomTkinter:** temas, botones y campos modernos, diseño adaptable.
5. **Archivos y persistencia:** guardar datos con JSON o CSV.
6. **Proyecto integrador:** aplicación de escritorio pequeña y útil.

Tkinter suele estar disponible con Python, aunque algunas distribuciones de Linux lo empaquetan por separado. CustomTkinter es externo y se instala en un entorno de proyecto.

## Preparación para CustomTkinter

En una terminal, dentro de la carpeta del proyecto:

```bash
python -m venv .venv
```

Activa el entorno virtual según tu sistema operativo y luego instala:

```bash
python -m pip install customtkinter
```

Comprueba la instalación ejecutando un archivo mínimo que importe `customtkinter`. Si falla, revisa que la terminal use el Python del entorno virtual.

## Proyectos en orden de dificultad

- **Inicial:** ventana con título, etiqueta y botón que cambia un mensaje.
- **Básico:** calculadora de dos números con validación.
- **Intermedio:** formulario de registro con campos obligatorios.
- **Intermedio+:** agenda o inventario pequeño guardado en JSON.
- **Integrador:** panel de seguimiento de un proyecto escolar con búsqueda y resumen.

## Reglas de diseño del código

- La interfaz presenta información; las funciones realizan los cálculos.
- Evita colocar todo el programa dentro de una sola función.
- Valida entradas y muestra errores comprensibles.
- No bloquees la ventana con tareas largas.
- Guarda los datos solo cuando sea necesario y explica dónde se almacenan.
- Prueba ventanas redimensionadas y resoluciones pequeñas.

## Retos

1. Cambia el texto y el tema de una ventana.
2. Añade un segundo botón y explica qué función ejecuta.
3. Evita que una calculadora se cierre si el usuario escribe texto en vez de un número.
4. Guarda y recupera una preferencia sencilla.
5. Explica qué parte del programa corresponde a la interfaz, a los datos y a la lógica.

## Documentación

- [Tkinter — documentación de Python](https://docs.python.org/es/3/library/tkinter.html)
- [CustomTkinter — documentación oficial](https://customtkinter.tomschimansky.com/)
