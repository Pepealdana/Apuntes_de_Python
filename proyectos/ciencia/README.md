# Proyecto de ciencia: trayectoria de un proyectil

Archivo: [simulacion_proyectil.py](simulacion_proyectil.py)

## Propósito

Explorar cómo cambian el alcance y la altura de un proyectil al modificar la velocidad inicial y el ángulo de lanzamiento.

## Preparación y ejecución

```bash
python -m pip install matplotlib
python proyectos/ciencia/simulacion_proyectil.py
```

Parámetros de ejemplo:

```bash
python proyectos/ciencia/simulacion_proyectil.py --velocidad 25 --angulo 35
```

El programa guarda una tabla CSV y una imagen PNG dentro de `salida_ciencia/`.

## Modelo y límites

El modelo supone terreno horizontal, gravedad constante y ausencia de resistencia del aire. Es útil para estudiar variables y gráficas, pero no representa todas las condiciones de un lanzamiento real.

## Retos

1. Compara ángulos de 30°, 45° y 60° manteniendo la velocidad.
2. Cambia la velocidad inicial y explica qué cambia en la trayectoria.
3. Añade un parámetro para la gravedad y compara dos valores.
4. Contrasta los resultados con la fórmula ideal del alcance.
5. Propón una medición real segura y explica qué factores harían diferir el experimento del modelo.

**Estado:** modelo y código incorporados; la interpretación científica debe considerar sus supuestos y límites.
