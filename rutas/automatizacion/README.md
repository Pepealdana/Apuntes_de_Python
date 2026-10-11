# Ruta: automatización y procesamiento de archivos

## Propósito

Usar Python para reducir tareas repetitivas: organizar archivos, procesar listas, transformar datos y generar reportes. Se empieza con módulos incluidos en Python para evitar instalaciones innecesarias.

## Herramientas

- `pathlib`: rutas y archivos.
- `shutil`: copiar y mover archivos.
- `csv`: leer y escribir tablas CSV.
- `json`: guardar y recuperar datos estructurados.
- `datetime`: fechas y horas.
- `logging`: registrar eventos y errores.
- `openpyxl`: solo si el proyecto necesita leer o crear archivos Excel.

## Progresión de proyectos

1. Leer un archivo de texto y contar líneas.
2. Analizar un CSV y calcular totales.
3. Clasificar archivos por extensión en una carpeta de prueba.
4. Generar un reporte con fecha y resumen.
5. Construir un proceso reutilizable con validaciones y registro de errores.

## Seguridad y buenas prácticas

- Practica primero en una carpeta con archivos de prueba.
- No borres ni sobrescribas archivos sin una confirmación clara.
- Antes de mover archivos, imprime un resumen de las acciones que se realizarán.
- Valida extensiones y nombres; gestiona archivos duplicados.
- No incluyas contraseñas, tokens ni datos personales reales en ejemplos.
- Usa rutas explícitas y explica desde qué carpeta se ejecuta el programa.

## Retos

- Añade una opción de simulación que muestre lo que haría el programa sin cambiar archivos.
- Registra cuántos archivos se procesaron y cuántos fallaron.
- Guarda un resumen en CSV o JSON.
- Permite elegir la carpeta mediante un argumento o una configuración sencilla.

## Referencias

- [pathlib](https://docs.python.org/es/3/library/pathlib.html)
- [shutil](https://docs.python.org/es/3/library/shutil.html)
- [csv](https://docs.python.org/es/3/library/csv.html)
- [json](https://docs.python.org/es/3/library/json.html)
