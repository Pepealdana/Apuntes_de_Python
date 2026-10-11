# Pruebas automáticas

La suite usa `unittest` y archivos temporales para evitar modificar datos de trabajo. Incluye pruebas de:

- Lectura y validación de CSV, informes y organización segura de archivos.
- Persistencia JSON de actividades.
- CRUD, validaciones y persistencia de las dos aplicaciones Flask.
- Redimensionamiento proporcional de imágenes con Pillow.
- Lectura de CSV y generación de gráficas con Matplotlib.
- Exportación CSV/gráfica de la simulación científica.
- Ejecución del clasificador Iris con scikit-learn.
- Estado inicial y posiciones del juego Pygame.

## Ejecutar en el equipo local

Desde la raíz del repositorio, crea un entorno virtual y activa el entorno según tu sistema. Para instalar las dependencias que necesita la suite:

```bash
python -m pip install -r requirements-test.txt
python -m compileall -q sesiones proyectos pruebas
python -m unittest discover -s pruebas -v
```

La automatización de GitHub Actions usa Python 3.12 y ejecuta esos mismos pasos. Los programas gráficos no abren ventanas durante las pruebas automatizadas.

## Pruebas manuales pendientes

En un equipo con escritorio, prueba además:

1. **CustomTkinter:** ejecutar la calculadora; probar campos vacíos, letras, decimales con coma y división por cero.
2. **Formulario:** guardar un registro ficticio, revisar el CSV y comprobar que no se sobrescriban los registros previos.
3. **Gestor JSON:** agregar y eliminar una actividad; cerrar y volver a abrir; comprobar persistencia. Después, probar con una copia de un JSON malformado y confirmar que no se sobrescriba.
4. **Pygame:** usar flechas y WASD, recoger estrellas, tocar obstáculos, perder las tres vidas, ganar, reiniciar y cerrar la ventana.
5. **Flask/API:** la suite prueba rutas con el cliente de pruebas de Flask; repetir también los comandos del README de la API en ejecución local.
6. **Imágenes, gráficas y ciencia:** abrir las salidas creadas y verificar dimensiones, ejes, etiquetas y contenido.

No uses datos personales reales ni imágenes sensibles. La suite automática no sustituye la comprobación de ventanas, teclado y visualización en el equipo donde se utilizarán.
