# Juego completo: Recolecta las estrellas

Archivo: [pygame_recolectar.py](pygame_recolectar.py)

## Objetivo

Recoger ocho estrellas amarillas antes de perder tres vidas, evitando los bloques rojos.

## Preparación y ejecución

```bash
python -m venv .venv
python -m pip install pygame
python proyectos/juegos/pygame_recolectar.py
```

Si necesitas activar el entorno virtual, consulta la [guía de entorno](../../GUIA_ENTORNO.md).

## Controles

- Flechas o WASD: mover al jugador azul.
- R: reiniciar después de ganar o perder.
- Cerrar la ventana: salir.

## Conceptos demostrados

- Bucle principal, eventos y control de FPS.
- Movimiento basado en el tiempo transcurrido.
- Límites de la pantalla y normalización de movimiento diagonal.
- Colisiones entre jugador, estrellas y obstáculos.
- Puntuación, vidas, condición de victoria y reinicio.
- Funciones para inicializar el estado y dibujar texto.

## Retos

1. Cambia el número de estrellas y de vidas.
2. Añade un cronómetro.
3. Haz que los obstáculos se muevan.
4. Añade una pantalla inicial con instrucciones.
5. Separa la lógica del juego en una clase y escribe pruebas para las funciones que no dependan de Pygame.

**Estado:** código incorporado; necesita una prueba interactiva en un equipo con entorno gráfico para validar controles, dificultad y presentación visual.
