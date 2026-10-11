# Plan de implementación y control de calidad

Este documento diferencia el código incorporado, las comprobaciones automatizadas y las pruebas manuales pendientes. No se marca una interfaz como probada visualmente por el hecho de que su archivo compile.

## Fase 1 — Fundamentos didácticos

- [x] Conservar los apuntes originales durante la migración.
- [x] Organizar las sesiones 1–12 y mantener sus ejemplos.
- [x] Añadir la práctica acumulativa «Aula organizada» sin reemplazar los ejercicios originales.
- [x] Crear una plantilla común para nuevas sesiones.
- [x] Revisar por lectura didáctica la correspondencia entre tema, ejemplo y retos de las 12 sesiones.
- [x] Añadir pruebas de humo para ejecutar los 13 ejemplos de consola con entradas controladas.
- [ ] Añadir ejercicios de repaso acumulativo después de las sesiones 4, 8 y 12.

## Fase 2 — Entorno y documentación

- [x] Documentar entornos virtuales, instalación de dependencias y errores frecuentes.
- [x] Mantener un catálogo de rutas aplicadas y proyectos.
- [x] Actualizar el README principal y el catálogo de proyectos.
- [x] Añadir el informe de auditoría didáctica y técnica.
- [x] Definir licencias separadas para material educativo y código.
- [ ] Documentar depuración en VS Code y uso básico de Git.
- [ ] Establecer una plantilla común de README para todos los proyectos nuevos.

## Fase 3 — Interfaces gráficas

- [x] Incorporar ejemplos Tkinter y CustomTkinter.
- [x] Incorporar calculadora, formulario CSV y gestor de actividades JSON.
- [x] Separar la lógica de operaciones de la calculadora para poder probarla sin abrir la ventana.
- [x] Probar la persistencia CSV del formulario y la persistencia JSON del gestor.
- [ ] Ejecutar ventanas en Windows y comprobar campos, botones, dimensiones y mensajes.
- [ ] Probar errores de permisos de escritura desde el entorno gráfico.

## Fase 4 — Pygame

- [x] Incorporar ejemplo de movimiento y juego de recolección.
- [x] Probar automáticamente el estado inicial del juego y la distribución inicial de elementos.
- [ ] Probar teclado, límites, colisiones repetidas, vidas, victoria, reinicio y cierre en escritorio real.
- [ ] Revisar visualmente dificultad, instrucciones y presentación en distintos tamaños de pantalla.

## Fase 5 — Automatización, CSV y gráficas

- [x] Mantener el modo de simulación predeterminado del organizador.
- [x] Probar la planificación y prevención de sobrescritura.
- [x] Probar lectura, validación y generación de informes CSV/TXT.
- [x] Probar la lectura de series y la exportación de gráficas.
- [x] Rechazar valores numéricos no finitos (NaN e infinito) en los procesadores de mediciones.
- [ ] Ejecutar el modo real del organizador solo con una carpeta temporal en Windows.
- [ ] Revisar manualmente los archivos CSV, TXT y PNG generados.
- [ ] Añadir pruebas específicas de permisos y errores de escritura.

## Fase 6 — Web, imágenes, ciencia e IA

- [x] Incorporar aplicación Flask y API REST local con persistencia JSON.
- [x] Probar operaciones CRUD, validación de datos y persistencia con el cliente de pruebas de Flask.
- [x] Probar redimensionamiento de imágenes, proporción y prevención de sobrescritura.
- [x] Probar generación de CSV y PNG de la simulación científica.
- [x] Probar ejecución del clasificador Iris y su reporte de métricas.
- [x] Rechazar valores no finitos en la calculadora, el simulador y los procesadores de mediciones.
- [ ] Probar Flask desde un navegador local y la API con `curl`.
- [ ] Probar Pillow con imágenes reales de diferentes formatos y orientaciones EXIF.
- [ ] Interpretar la matriz de confusión del clasificador con estudiantes.
- [ ] Comparar la simulación con cálculos independientes y discutir sus supuestos.

## Fase 7 — Validación de publicación

- [x] Añadir pruebas de humo de los ejemplos de las 12 sesiones.
- [x] Ampliar las pruebas de lógica, persistencia, entradas inválidas y generación de archivos.
- [x] Actualizar README, catálogo de proyectos y documentación de auditoría.
- [x] Confirmar GitHub Actions para esta revisión: [ejecución #47](https://github.com/Pepealdana/Apuntes_de_Python/actions/runs/38158313719), con 30 pruebas aprobadas.
- [ ] Completar el checklist manual de Windows incluido en `AUDITORIA_DIDACTICA_Y_TECNICA.md`.
- [ ] Actualizar este plan y el informe con los resultados reales de las pruebas manuales.

## Criterios para declarar un proyecto verificado

1. El código se ejecuta en el entorno documentado.
2. Se prueba el flujo principal.
3. Se prueban los casos de error relevantes.
4. Las instrucciones de instalación y ejecución coinciden con el comportamiento observado.
5. Se revisan los archivos generados o la interfaz visual.
6. Se documentan limitaciones y riesgos conocidos.

La compilación de sintaxis y las pruebas unitarias son evidencia útil, pero no sustituyen la validación de escritorio, el navegador ni la interacción con hardware.
