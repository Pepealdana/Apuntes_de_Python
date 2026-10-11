# Pruebas automáticas

Las pruebas usan `unittest`, incluido en Python, y archivos temporales para no modificar los datos de trabajo.

Desde la raíz del repositorio ejecuta:

```bash
python -m unittest discover -s pruebas -v
```

La suite actual cubre la validación de CSV, la generación de informes y la planificación segura del organizador de archivos. No mueve archivos reales ni requiere instalar bibliotecas externas.

La suite debe crecer con pruebas para la persistencia JSON, validaciones de formularios y funciones matemáticas. Las interfaces gráficas y Pygame requieren además pruebas manuales en un entorno con escritorio.
