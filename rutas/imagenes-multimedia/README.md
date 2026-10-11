# Ruta: imágenes y multimedia

## Propósito

Procesar imágenes con Python para comprender archivos, dimensiones, formatos y transformaciones básicas.

## Herramienta principal

Pillow, una biblioteca externa para abrir, redimensionar, recortar, convertir y guardar imágenes.

Instalación dentro del entorno virtual:

```bash
python -m pip install pillow
```

## Proyectos graduados

1. Mostrar el formato y las dimensiones de una imagen.
2. Redimensionar una copia sin sobrescribir el original.
3. Crear miniaturas para un conjunto de imágenes.
4. Convertir formatos compatibles y registrar los archivos generados.
5. Crear una herramienta sencilla con interfaz gráfica para elegir una imagen y aplicar una transformación.

## Buenas prácticas

- Conserva siempre el archivo original.
- Comprueba que el archivo existe y que el formato puede abrirse.
- Evita cargar imágenes enormes sin considerar la memoria disponible.
- Respeta licencias y derechos de autor de las imágenes usadas.
- Explica la diferencia entre cambiar dimensiones y cambiar el formato.

## Referencia

- [Pillow — documentación oficial](https://pillow.readthedocs.io/)
