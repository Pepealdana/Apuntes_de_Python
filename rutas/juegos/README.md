# Ruta: juegos 2D con Python

## Propósito

Construir juegos pequeños para aprender eventos, coordenadas, movimiento, colisiones, puntuación y organización del código. La ruta empieza con dibujos sencillos y avanza hacia Pygame.

## Secuencia

1. **Turtle:** movimiento y coordenadas sin instalar paquetes adicionales.
2. **Conceptos de juego:** ventana, pantalla, objetos, entrada, reglas y condición de victoria.
3. **Pygame:** inicialización, ventana, eventos, reloj y dibujo.
4. **Movimiento:** posición, velocidad y límites de pantalla.
5. **Interacción:** teclado, colisiones, puntuación y reinicio.
6. **Proyecto integrador:** Pong, laberinto, juego de recoger objetos o quiz visual.

## Instalación

Se recomienda crear un entorno virtual dentro del proyecto y ejecutar:

```bash
python -m pip install pygame
```

Comprueba la instalación con `python -c "import pygame; print(pygame.version.ver)"`. Si falla, revisa la [guía de entorno](../../GUIA_ENTORNO.md) y confirma que el paquete se instaló en el mismo intérprete que ejecuta el juego.

## Proyectos graduados

- Inicial: ventana que se cierra correctamente al pulsar el botón de cerrar.
- Básico: mover un objeto con las flechas.
- Intermedio: recoger objetos y sumar puntos.
- Intermedio+: añadir obstáculos, vidas y reinicio.
- Integrador: juego con menú, instrucciones, reglas y pantalla final.

## Conceptos importantes

- El bucle principal procesa eventos y actualiza la pantalla.
- La velocidad debe relacionarse con el tiempo para que el movimiento sea consistente.
- Las colisiones deben probarse en los bordes y en situaciones límite.
- El juego debe poder cerrarse sin forzar la terminación del proceso.
- Empieza con figuras dibujadas; incorpora imágenes y sonidos solo después de que funcione la lógica.

## Retos

1. Cambia el tamaño de la ventana y la velocidad del jugador.
2. Impide que el objeto salga de la pantalla.
3. Añade una meta y detecta cuándo se alcanza.
4. Agrega puntuación y una condición de derrota.
5. Explica qué hace cada parte del bucle del juego.

## Documentación

- [Documentación oficial de Pygame](https://www.pygame.org/docs/)
- [Tutoriales oficiales de Pygame](https://www.pygame.org/docs/)
