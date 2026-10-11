# Automatización y datos de prueba

## 1. Organizador de archivos

Archivo: [organizar_archivos.py](organizar_archivos.py)

Clasifica archivos por extensión. Por seguridad, el modo predeterminado solo muestra una simulación. Para realizar movimientos reales se requiere añadir explícitamente `--aplicar`.

Prueba con una carpeta temporal que contenga archivos ficticios:

```bash
python proyectos/automatizacion/organizar_archivos.py carpeta_prueba
python proyectos/automatizacion/organizar_archivos.py carpeta_prueba --aplicar
```

No ejecutes la segunda orden sobre carpetas importantes sin revisar primero la simulación.

## 2. Reporte CSV

Archivo: [reporte_csv.py](reporte_csv.py)

Usa la biblioteca estándar para calcular un resumen básico. Si no encuentra un CSV de ejemplo, crea uno ficticio sin sobrescribir un archivo que ya exista.

## 3. Informe de mediciones

Archivo: [reporte_mediciones.py](../datos/reporte_mediciones.py)  
Datos ficticios: [mediciones_prueba.csv](../datos/mediciones_prueba.csv)

Desde la raíz del repositorio:

```bash
python proyectos/datos/reporte_mediciones.py
```

Genera una carpeta `salida_reporte` con un CSV resumido y un informe de texto. Las filas con campos vacíos o mediciones inválidas se informan y se omiten.

## Retos

- Añade un modo de simulación al organizador que exporte el plan a CSV.
- Permite elegir la columna numérica en el reporte.
- Añade una validación de fecha.
- Compara los resultados de dos grupos y explica por qué el promedio por sí solo no describe toda la distribución.

**Estado:** ejemplos incorporados. Prueba primero con archivos ficticios y verifica los archivos generados antes de usar datos propios.
