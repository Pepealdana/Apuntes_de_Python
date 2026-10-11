# Plan de implementación del repositorio

Este plan distingue entre guías y código incorporados, comprobaciones automáticas y pruebas prácticas pendientes. La presencia de un archivo no demuestra que se haya ejecutado correctamente en un equipo de escritorio.

## Fase 1 — Fundamentos

- [x] Mantener las sesiones 1–12 como ruta inicial.
- [x] Conservar los apuntes originales durante la migración.
- [x] Mantener una comprobación automática de sintaxis.
- [x] Añadir una práctica acumulativa que evoluciona de variables a un proyecto con JSON a lo largo de las sesiones 1–12.
- [ ] Revisar cada ejemplo Python contra su explicación y corregir posibles discrepancias.
- [ ] Homogeneizar los criterios de logro y los cierres de las doce sesiones.
- [ ] Añadir ejercicios de repaso acumulativo después de las sesiones 4, 8 y 12.

## Fase 2 — Organización y herramientas

- [x] Definir una ruta general de aprendizaje.
- [x] Crear un catálogo de rutas aplicadas.
- [x] Añadir una guía de entornos virtuales, pip y errores de instalación.
- [ ] Documentar depuración en VS Code, pruebas con unittest y uso básico de Git.
- [ ] Establecer una plantilla común para nuevos proyectos.

## Fase 3 — CustomTkinter

- [x] Ejemplo inicial de CustomTkinter.
- [x] Calculadora con suma, resta, multiplicación, división y validación.
- [x] Formulario con campos obligatorios y almacenamiento CSV.
- [x] Gestor de actividades con lectura, escritura y eliminación en JSON.
- [ ] Ejecutar cada ventana en un entorno gráfico real.
- [ ] Probar entradas inválidas, archivos JSON dañados y errores de escritura.
- [ ] Mejorar el selector de registros del gestor JSON y añadir confirmación antes de eliminar.

## Fase 4 — Pygame

- [x] Ejemplo inicial de movimiento.
- [x] Juego de recolección con colisiones, puntuación, vidas, victoria y reinicio.
- [ ] Ejecutar el juego e inspeccionar la dificultad y la respuesta del teclado.
- [ ] Probar colisiones repetidas, reinicio y cierre de ventana.
- [ ] Añadir pantalla inicial y pruebas de lógica separadas del bucle gráfico.

## Fase 5 — Automatización y datos

- [x] Organizador de archivos con modo simulación predeterminado.
- [x] Informe CSV que valida filas y genera resumen de texto y CSV.
- [x] Archivo de mediciones ficticias con registros válidos y filas defectuosas.
- [x] Gráfica basada en CSV con avisos por filas omitidas.
- [ ] Ejecutar sobre una carpeta temporal y comparar los resultados con cálculos manuales.
- [ ] Añadir pruebas automatizadas para CSV vacío, columnas faltantes, datos inválidos y rutas inexistentes.
- [ ] Documentar salidas generadas y evitar subir datos personales reales.

## Fase 6 — Web, imágenes, ciencia e IA

- [x] Aplicación local Flask para agregar, consultar, completar y eliminar tareas con persistencia JSON.
- [x] Herramienta Pillow que redimensiona una copia de imagen sin sobrescribir por defecto.
- [x] Simulación de proyectil con CSV y gráfica, indicando los supuestos del modelo.
- [x] Clasificador Iris con scikit-learn, conjunto de prueba y métricas.
- [ ] Ejecutar y probar las rutas de la aplicación Flask.
- [ ] Probar Pillow con imágenes reales de distintos formatos y orientaciones.
- [ ] Comparar la simulación con cálculos independientes.
- [ ] Ejecutar el clasificador y explicar la matriz de confusión y los límites de las métricas.
- [ ] Añadir pruebas automatizadas a la lógica que no dependa de ventanas ni de servicios externos.
- [ ] Crear una aplicación consumidora de una API pública con timeout, manejo de errores y fuente de datos documentada.

## Fase 7 — Calidad y proyectos integradores

- [ ] Crear pruebas unitarias para funciones de cálculo, validación, lectura y escritura.
- [ ] Añadir una plantilla común de README para cada proyecto.
- [ ] Registrar versiones de Python y dependencias una vez realizadas pruebas locales.
- [ ] Añadir un proyecto integrador que conecte interfaz gráfica, JSON y visualización.
- [ ] Mantener comunicación serial con Arduino como una ruta opcional, no como requisito para aprender Python.

## Criterios para marcar un proyecto como verificado

Un proyecto solo se marcará como verificado cuando:
1. el código se haya ejecutado en el entorno indicado;
2. se haya probado el flujo principal;
3. se hayan probado al menos los casos de error relevantes;
4. las instrucciones de instalación y ejecución coincidan con lo observado;
5. las salidas generadas se hayan revisado;
6. cualquier limitación conocida quede documentada.

La comprobación automática de sintaxis no demuestra que una interfaz se vea correctamente ni que un juego, una aplicación web o una biblioteca externa funcione en el equipo del estudiante.
