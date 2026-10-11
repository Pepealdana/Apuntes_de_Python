# Proyectos de interfaces gráficas

## 1. Calculadora con CustomTkinter

Archivo: [calculadora_customtkinter.py](calculadora_customtkinter.py)

Realiza suma, resta, multiplicación y división. Valida entradas, acepta coma o punto decimal, contempla división por cero y permite limpiar los campos. La lógica aritmética está separada de la ventana para poder probarla automáticamente.

## 2. Formulario con validación y CSV

Archivo: [formulario_estudiantes.py](formulario_estudiantes.py)

Exige nombre y curso y agrega registros al CSV sin reemplazar los anteriores. Los ejemplos deben practicarse con nombres ficticios, no con datos personales de estudiantes.

## 3. Gestor de actividades con JSON

Archivo: [gestor_actividades_json.py](gestor_actividades_json.py)

Permite agregar, consultar y eliminar actividades almacenadas en JSON. Incluye confirmación antes de eliminar y evita guardar cambios si el archivo inicial tiene una estructura inválida o no se puede leer.

## Preparación

Desde la raíz del repositorio, crea un entorno virtual e instala la dependencia:

```bash
python -m venv .venv
python -m pip install customtkinter
```

Activa el entorno según tu sistema operativo siguiendo la [guía general](../../GUIA_ENTORNO.md).

## Ejecutar

Ejemplo desde la raíz:

```bash
python proyectos/interfaces/calculadora_customtkinter.py
python proyectos/interfaces/formulario_estudiantes.py
python proyectos/interfaces/gestor_actividades_json.py
```

Los archivos JSON y CSV se crean en el directorio de trabajo desde el que se lanza el programa, no necesariamente en la carpeta del script.

## Retos de ampliación

- Calculadora: añadir historial o permitir seleccionar la precisión de salida.
- Formulario: listar registros existentes y añadir filtros.
- Gestor JSON: incorporar edición y búsqueda.
- En todos los proyectos: separar más lógica de negocio de la interfaz y añadir pruebas a funciones independientes de la ventana.

**Estado:** la lógica de persistencia y las operaciones de la calculadora tienen pruebas automatizadas. La presentación visual y la interacción de las ventanas deben probarse en un entorno gráfico real.
