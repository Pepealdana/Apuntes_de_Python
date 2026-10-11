# Preparar el entorno de Python

Esta guía explica cómo ejecutar los proyectos del repositorio sin instalar todas las bibliotecas en el Python global del equipo.

## 1. Comprobar Python

En Visual Studio Code, abre una terminal y ejecuta:

```bash
python --version
```

En algunos equipos Windows puede ser necesario usar:

```powershell
py --version
```

Usa un intérprete de Python 3 compatible con el proyecto. Si ambos comandos existen, comprueba cuál estás usando en VS Code.

## 2. Crear un entorno virtual

Desde la carpeta del proyecto:

```bash
python -m venv .venv
```

Si el comando `python` no funciona en Windows, prueba `py -m venv .venv`.

### Activar en Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Activar en Windows CMD

```bat
.venv\Scripts\activate.bat
```

### Activar en macOS o Linux

```bash
source .venv/bin/activate
```

Cuando el entorno esté activo, instala los paquetes con `python -m pip`. Para salir del entorno, ejecuta `deactivate`.

Si PowerShell bloquea la activación por su política de ejecución, puedes abrir una terminal CMD o seleccionar el intérprete `.venv` desde VS Code; no cambies la política del equipo sin comprender el efecto.

## 3. Instalar solo lo necesario

Ejecuta únicamente la instrucción de la biblioteca que necesita tu proyecto:

| Proyecto | Instalación |
|---|---|
| Tkinter | Normalmente viene con Python; algunas distribuciones Linux lo empaquetan por separado |
| CustomTkinter | `python -m pip install customtkinter` |
| Pygame | `python -m pip install pygame` |
| Matplotlib | `python -m pip install matplotlib` |
| Pillow | `python -m pip install pillow` |
| Requests | `python -m pip install requests` |

No necesitas instalar todos estos paquetes al comenzar. Si un proyecto no los usa, no los instales.

## 4. Comprobar una instalación

Para CustomTkinter:

```bash
python -c "import customtkinter; print('CustomTkinter listo')"
```

Para Pygame:

```bash
python -c "import pygame; print(pygame.version.ver)"
```

Para Matplotlib:

```bash
python -c "import matplotlib; print(matplotlib.__version__)"
```

Si aparece `ModuleNotFoundError`, normalmente el paquete no está instalado en el mismo intérprete que ejecuta el programa. Comprueba el intérprete seleccionado en VS Code y repite la instalación con ese entorno activo.

## 5. Ejecutar un archivo

Desde la carpeta del proyecto:

```bash
python nombre_del_archivo.py
```

Sustituye el nombre por el archivo real. En proyectos con ventanas o juegos, el equipo debe disponer de un entorno gráfico compatible.

## 6. Errores frecuentes

- **Se instaló la biblioteca, pero no se encuentra:** el terminal usa otro Python o el entorno virtual no está activo.
- **El comando `python` no existe:** prueba `py` en Windows y selecciona el intérprete correcto en VS Code.
- **La ventana no abre en un servidor o terminal sin escritorio:** Tkinter, CustomTkinter y Pygame requieren una sesión gráfica.
- **No hay permisos de instalación:** crea el entorno virtual en una carpeta donde tengas permisos; no intentes modificar instalaciones del sistema.
- **El proyecto funciona en un equipo y en otro no:** registra versión de Python, sistema operativo, biblioteca y mensaje de error.

## 7. Buenas prácticas para el repositorio

- No subas la carpeta `.venv` a GitHub.
- No incluyas contraseñas ni claves de API en el código.
- Registra las dependencias de cada proyecto cuando se conviertan en parte estable del trabajo.
- Comparte los mensajes de error completos al pedir ayuda, pero oculta datos personales o secretos.
