"""Mueve un rectángulo con las flechas del teclado.

Preparación:
    python -m pip install pygame

Controles:
    Flechas del teclado: mover el rectángulo.
    Cerrar la ventana: terminar el juego.
"""

import pygame


ANCHO = 640
ALTO = 400
TAMANO = 40
VELOCIDAD = 240  # píxeles por segundo


def limitar(valor, minimo, maximo):
    """Mantiene un valor dentro de los límites indicados."""
    return max(minimo, min(valor, maximo))


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Primer movimiento con Pygame")
    reloj = pygame.time.Clock()

    x = (ANCHO - TAMANO) / 2
    y = (ALTO - TAMANO) / 2
    ejecutando = True

    while ejecutando:
        # El tiempo transcurrido permite mantener una velocidad coherente.
        delta = reloj.tick(60) / 1000

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            x -= VELOCIDAD * delta
        if teclas[pygame.K_RIGHT]:
            x += VELOCIDAD * delta
        if teclas[pygame.K_UP]:
            y -= VELOCIDAD * delta
        if teclas[pygame.K_DOWN]:
            y += VELOCIDAD * delta

        x = limitar(x, 0, ANCHO - TAMANO)
        y = limitar(y, 0, ALTO - TAMANO)

        pantalla.fill((24, 34, 52))
        pygame.draw.rect(
            pantalla,
            (245, 166, 35),
            pygame.Rect(round(x), round(y), TAMANO, TAMANO),
            border_radius=8,
        )
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
