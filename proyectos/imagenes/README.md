# Proyecto: redimensionar imágenes con Pillow

Archivo: [redimensionar_imagen.py](redimensionar_imagen.py)

## Propósito

Abrir una imagen, conservar su proporción, redimensionarla y guardar una copia en otra carpeta sin alterar el archivo original.

## Preparación

```bash
python -m pip install pillow
python proyectos/imagenes/redimensionar_imagen.py ruta/a/tu_imagen.jpg --ancho 400
```

El archivo de entrada debe existir. Por defecto, la copia se guarda en `imagenes_generadas/`. Si el destino ya existe, el programa se detiene para evitar reemplazarlo sin permiso. La opción `--sobrescribir` autoriza ese reemplazo explícitamente.

## Retos

1. Cambia el ancho y compara las dimensiones.
2. Prueba con PNG y JPEG.
3. Añade una opción para crear miniaturas cuadradas.
4. Procesa una carpeta completa, omitiendo archivos que no sean imágenes.
5. Añade un informe CSV con archivo original, dimensiones originales y dimensiones nuevas.

**Estado:** código incorporado; requiere pruebas con imágenes reales de diferentes formatos. No se incluyen imágenes de terceros como si fueran propias.
