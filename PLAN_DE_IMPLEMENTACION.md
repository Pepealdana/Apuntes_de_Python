# Plan de implementación del repositorio

Este plan distingue entre guías y código incorporados, comprobaciones automáticas y pruebas prácticas pendientes. La presencia de un archivo no demuestra que se haya ejecutado correctamente en un equipo de escritorio.

## Fase 1 — Fundamentos

- [x] Mantener las sesiones 1–12 como ruta inicial.
- [x] Conservar los apuntes originales durante la migración.
- [x] Mantener una comprobación automática de sintaxis.
- [x] Añadir una práctica acumulativa que evoluciona de variables a un proyecto con JSON a lo largo de las sesiones 1–12.
- [x] Añadir una plantilla didáctica común y enlazarla desde el índice de sesiones.
- [ ] Revisar cada ejemplo Python contra su explicación y corregir posibles discrepancias.
- [ ] Añadir ejercicios de repaso acumulativo después de las sesiones 4, 8 y 12.

## Fase 2 — Organización y herramientas

- [x] Definir una ruta general de aprendizaje.
- [x] Crear un catálogo de rutas aplicadas.
- [x] Añadir una guía de entornos virtuales, pip y errores de instalación.
- [x] Crear pruebas iniciales con la biblioteca estándar.
- [x] Configurar GitHub Actions para compilar sesiones, proyectos y pruebas y ejecutar `unittest`.
- [x] Confirmar una ejecución correcta de GitHub Actions; la suite se amplió y quedó configurada para Python 3.12. La ejecución más reciente de la suite ampliada debe volver a confirmarse tras cada cambio.
- [ ] Documentar depuración en VS Code y uso básico de Git.
- [ ] Establecer una plantilla común de README para nuevos proyectos.

## Fase 3 — CustomTkinter

- [x] Ejemplo inicial de CustomTkinter.
- [x] Calculadora con suma, resta, multiplicación, división y validación.
- [x] Formulario con campos obligatorios y almacenamiento CSV.
- [x] Gestor de actividades con lectura, escritura y eliminación en JSON.
- [x] Selector de actividad y confirmación antes de eliminar; evitar guardar si el JSON inicial está dañado.
- [ ] Ejecutar cada ventana en un entorno gráfico real.
- [x] Añadir pruebas automáticas de lectura/escritura JSON y estructura incorrecta.\n- [ ] Probar ventanas, entradas inválidas y errores de escritura en escritorio real.

## Fase 4 — Pygame

- [x] Ejemplo inicial de movimiento.
- [x] Juego de recolección con colisiones, puntuación, vidas, victoria y reinicio.
- [ ] Ejecutar el juego e inspeccionar la dificultad y la respuesta del teclado.
- [ ] Probar colisiones repetidas, reinicio y cierre de ventana.
- [x] Añadir una prueba automatizada del estado inicial y la distribución de elementos fuera del bucle gráfico.\n- [ ] Añadir pantalla inicial y probar teclado, colisiones, reinicio y cierre en escritorio real.

## Fase 5 — Automatización y datos

- [x] Organizador de archivos con modo simulación predeterminado.
- [x] Informe CSV que valida filas y genera resumen de texto y CSV.
- [x] Archivo de mediciones ficticias con registros válidos y filas defectuosas.
- [x] Gráfica basada en CSV con avisos por filas omitidas.
- [x] Pruebas unitarias para validación CSV, informes y planificación segura de archivos.\n- [x] Añadir pruebas para lectura de series y generación de gráficas con CSV de prueba.
- [x] Automatizar el procesamiento de CSV de prueba y la generación de una gráfica en archivos temporales.\n- [ ] Comparar los resultados de negocio con cálculos manuales y revisar salidas en el equipo local.
- [ ] Añadir pruebas para CSV vacío, columnas faltantes, rutas inexistentes y errores de escritura.
- [ ] Documentar salidas generadas y evitar subir datos personales reales.

## Fase 6 — Web, imágenes, ciencia e IA

- [x] Aplicación local Flask para agregar, consultar, completar y eliminar tareas con persistencia JSON.
- [x] API REST local con GET, POST, PATCH y DELETE, validación y persistencia JSON.
- [x] Herramienta Pillow que redimensiona una copia de imagen sin sobrescribir por defecto.
- [x] Simulación de proyectil con CSV y gráfica, indicando los supuestos del modelo.
- [x] Clasificador Iris con scikit-learn, conjunto de prueba y métricas.
- [x] Pruebas unitarias para las reglas matemáticas de la trayectoria ideal.
- [x] Añadir pruebas de rutas CRUD, validaciones y persistencia JSON para la aplicación Flask y la API REST.\n- [ ] Repetir el flujo desde navegador y cliente HTTP en ejecución local.
- [x] Añadir pruebas automáticas de redimensionamiento, proporción y prevención de sobrescritura.\n- [ ] Probar imágenes reales de distintos formatos y orientaciones en el equipo local.
- [x] Añadir prueba de integración para exportar CSV y gráfica científica.\n- [ ] Comparar la simulación con cálculos independientes.
- [x] Añadir prueba automatizada de ejecución del clasificador y generación de métricas.\n- [ ] Revisar los resultados del clasificador y explicar la matriz de confusión.
- [ ] Añadir un cliente de API pública con timeout, manejo de errores y fuente de datos documentada.

## Fase 7 — Calidad y proyectos integradores

- [x] Ampliar las pruebas a JSON, rutas Flask/API, imágenes, gráficas, ciencia, clasificador y lógica inicial de Pygame.\n- [ ] Añadir casos de error adicionales para archivos corruptos, permisos y rutas inexistentes.
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

La comprobación automática de sintaxis y las pruebas unitarias no demuestran que una interfaz se vea correctamente ni que un juego, una aplicación web o una biblioteca externa funcione en el equipo del estudiante.
