# Proyectos de interfaces gráficas

## 1. Calculadora con CustomTkinter

Archivo: [calculadora_customtkinter.py](calculadora_customtkinter.py)

Operaciones de suma, resta, multiplicación y división. Valida números, contempla división por cero y permite limpiar los campos.

## 2. Formulario con validación y CSV

Archivo: [formulario_estudiantes.py](formulario_estudiantes.py)

Formulario de ejemplo que exige nombre y curso y agrega los registros a un CSV sin reemplazar los anteriores. Usa nombres y datos ficticios al practicar.

## 3. Gestor de actividades con JSON

Archivo: [gestor_actividades_json.py](gestor_actividades_json.py)

Aplicación para agregar, consultar y eliminar actividades almacenadas en JSON. Demuestra persistencia entre ejecuciones y manejo inicial de errores de lectura.

## Preparación

Desde la carpeta del repositorio, crea un entorno virtual y ejecuta:

```bash
python -m venv .venv
python -m pip install customtkinter
```

Activa el entorno según tu sistema operativo siguiendo la [guía general](../../GUIA_ENTORNO.md).

Ejecuta un archivo, por ejemplo:

```bash
python proyectos/interfaces/calculadora_customtkinter.py
```

El archivo JSON o CSV se crea en el directorio de trabajo desde el que se lanza el programa, no necesariamente en la carpeta del script.

## Retos de ampliación

- Calculadora: permitir operar con una expresión a la vez y añadir historial.
- Formulario: listar registros existentes y añadir filtros.
- Gestor JSON: incorporar edición, confirmación antes de eliminar y búsqueda.
- En todos los proyectos: separar la lógica de negocio de la interfaz y añadir pruebas a las funciones que no dependen de la ventana.

**Estado:** ejemplos incorporados; la ejecución de las ventanas y el comportamiento en distintos sistemas deben verificarse en un entorno gráfico real.
