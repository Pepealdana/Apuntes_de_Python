# Sesión 10. Guardar y recuperar información

**Nivel:** inicial-intermedio  
**Requisitos previos:** sesiones 1 a 9  
**Herramientas:** Python 3 y Visual Studio Code  
**Producto:** un programa que guarda información en archivos de texto, CSV y JSON.

## Objetivo

Leer y escribir archivos de forma controlada y reconocer cuándo conviene usar texto plano, CSV o JSON.

## 1. Conceptos clave

### Abrir archivos con `with`

La instrucción `with` cierra el archivo automáticamente al terminar el bloque.

```python
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Estoy aprendiendo Python.\n")
```

Modos iniciales:
- `"r"`: leer un archivo existente.
- `"w"`: escribir y reemplazar el contenido anterior.
- `"a"`: añadir contenido al final.
- `"x"`: crear un archivo nuevo y fallar si ya existe.

Usa `encoding="utf-8"` para trabajar mejor con tildes y otros caracteres.

### Leer texto

```python
with open("notas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)
```

La ruta relativa se interpreta desde el directorio de trabajo del programa. En proyectos reales conviene controlar las rutas y no asumir que el programa siempre se ejecutará desde la misma carpeta.

### CSV: datos tabulares

CSV permite almacenar filas y columnas. Python incluye el módulo estándar `csv`.

```python
import csv

with open("mediciones.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["sensor", "temperatura"])
    escritor.writerow(["A1", 23.5])
```

### JSON: datos estructurados

JSON representa objetos y listas y es frecuente en APIs y archivos de configuración.

```python
import json

configuracion = {"proyecto": "Estación escolar", "activa": True}

with open("configuracion.json", "w", encoding="utf-8") as archivo:
    json.dump(configuracion, archivo, ensure_ascii=False, indent=2)
```

Al leer JSON con `json.load()`, se recuperan tipos de datos compatibles como diccionarios, listas, cadenas, números y booleanos.

## 2. Ejemplo guiado

Ejecuta [10_archivos_datos.py](ejemplos/10_archivos_datos.py). El programa crea una carpeta `salida_sesion10` en el directorio desde el que se ejecuta y escribe ejemplos de texto, CSV y JSON.

No guardes contraseñas, tokens ni datos personales sensibles en los archivos de práctica.

## 3. Experimenta

1. Cambia el mensaje guardado en el archivo de texto.
2. Añade una segunda fila al CSV.
3. Agrega una clave al diccionario que se guarda en JSON.
4. Abre los archivos generados con un editor de texto y compara su formato.

## 4. Retos

### Reto 1 — Diario de aprendizaje

Solicita una frase y añádela a un archivo de texto sin borrar las entradas anteriores.

### Reto 2 — Registro de mediciones

Guarda tres mediciones en un CSV con encabezados.

### Reto 3 — Configuración de proyecto

Guarda en JSON el nombre de un proyecto, su estado y una lista de tareas.

## 5. Errores frecuentes

- Usar `"w"` cuando se quería añadir datos: este modo reemplaza el contenido.
- Intentar leer un archivo que no existe.
- Olvidar `encoding="utf-8"`.
- Confundir un archivo CSV tabular con JSON estructurado.
- Guardar datos sensibles en repositorios públicos.

## 6. Cierre

1. ¿Qué diferencia hay entre los modos `r`, `w` y `a`?
2. ¿Cuándo usarías CSV y cuándo JSON?
3. ¿Por qué es útil abrir archivos con `with`?

## Criterios de logro

- [ ] Escribo y leo un archivo de texto.
- [ ] Creo un CSV con filas.
- [ ] Guardo datos estructurados en JSON.
- [ ] Distingo modos de apertura y evito sobrescribir datos accidentalmente.

## Próxima sesión

**Errores y excepciones:** responder de forma controlada cuando algo falla.


## Práctica acumulativa — Proyecto: Aula organizada

Guarda y recupera las actividades en JSON. Como extensión, exporta una tabla CSV para abrirla en una hoja de cálculo. No sobrescribas archivos de usuario sin avisar y conserva una copia de los datos de prueba.

**Criterio de revisión:** el programa puede recuperar los registros en otra ejecución y trata de forma comprensible el caso en que el archivo todavía no existe.

**Evidencia:** guarda dos actividades, cierra el programa y vuelve a ejecutarlo para comprobar que los datos se recuperan.
