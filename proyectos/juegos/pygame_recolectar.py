"""Juego 2D: recoge estrellas y evita los obstáculos.

Instalación:
    python -m pip install pygame

Controles:
    Flechas o WASD: mover al jugador.
    R: reiniciar al terminar.
    Cerrar ventana: salir.
"""

import random
import pygame


ANCHO, ALTO = 720, 480
TAM_JUGADOR = 30
VELOCIDAD = 250
TOTAL_ESTRELLAS = 8
VIDAS_INICIALES = 3
FPS = 60

FONDO = (22, 31, 48)
BLANCO = (240, 244, 248)
AZUL = (65, 150, 245)
AMARILLO = (255, 200, 65)
ROJO = (230, 75, 80)
VERDE = (90, 205, 140)


def nueva_posicion(tamano, evitar=None):
    """Genera una posición dentro de la ventana, lejos del borde."""
    evitar = evitar or []
    for _ in range(100):
        rect = pygame.Rect(
            random.randint(45, ANCHO - tamano - 15),
            random.randint(65, ALTO - tamano - 15),
            tamano,
            tamano,
        )
        if all(not rect.colliderect(otro.inflate(45, 45)) for otro in evitar):
            return rect
    return pygame.Rect(ANCHO // 2, ALTO // 2, tamano, tamano)


def reiniciar():
    jugador = pygame.Rect(ANCHO // 2, ALTO // 2, TAM_JUGADOR, TAM_JUGADOR)
    obstaculos = []
    for _ in range(4):
        obstaculos.append(nueva_posicion(32, [jugador, *obstaculos]))
    estrella = nueva_posicion(20, [jugador, *obstaculos])
    return jugador, obstaculos, estrella, 0, VIDAS_INICIALES, False


def dibujar_texto(pantalla, fuente, texto, posicion, color=BLANCO):
    pantalla.blit(fuente.render(texto, True, color), posicion)


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Recolecta las estrellas")
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(None, 28)
    fuente_grande = pygame.font.Font(None, 48)

    jugador, obstaculos, estrella, puntos, vidas, terminado = reiniciar()
    ejecutando = True

    while ejecutando:
        delta = min(reloj.tick(FPS) / 1000, 0.05)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_r and terminado:
                jugador, obstaculos, estrella, puntos, vidas, terminado = reiniciar()

        teclas = pygame.key.get_pressed()
        if not terminado:
            dx = int(teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) - int(teclas[pygame.K_LEFT] or teclas[pygame.K_a])
            dy = int(teclas[pygame.K_DOWN] or teclas[pygame.K_s]) - int(teclas[pygame.K_UP] or teclas[pygame.K_w])
            # Normalizar movimiento diagonal para no ganar velocidad extra.
            if dx and dy:
                factor = 0.70710678
            else:
                factor = 1.0
            jugador.x += round(dx * VELOCIDAD * factor * delta)
            jugador.y += round(dy * VELOCIDAD * factor * delta)
            jugador.clamp_ip(pantalla.get_rect())

            if jugador.colliderect(estrella):
                puntos += 1
                estrella = nueva_posicion(20, [jugador, *obstaculos])
                if puntos >= TOTAL_ESTRELLAS:
                    terminado = True

            for obstaculo in obstaculos:
                if jugador.colliderect(obstaculo):
                    vidas -= 1
                    jugador.center = (ANCHO // 2, ALTO // 2)
                    if vidas <= 0:
                        terminado = True
                    break

        pantalla.fill(FONDO)
        pygame.draw.rect(pantalla, AZUL, jugador, border_radius=7)
        pygame.draw.rect(pantalla, AMARILLO, estrella, border_radius=10)
        for obstaculo in obstaculos:
            pygame.draw.rect(pantalla, ROJO, obstaculo, border_radius=5)

        dibujar_texto(pantalla, fuente, f"Puntos: {puntos}/{TOTAL_ESTRELLAS}", (18, 16))
        dibujar_texto(pantalla, fuente, f"Vidas: {vidas}", (ANCHO - 110, 16), VERDE if vidas > 1 else ROJO)
        dibujar_texto(pantalla, fuente, "Mueve con flechas o WASD; evita los bloques rojos.", (18, ALTO - 30))

        if terminado:
            mensaje = "¡Ganaste!" if puntos >= TOTAL_ESTRELLAS else "Fin del juego"
            superficie = fuente_grande.render(mensaje, True, AMARILLO if puntos >= TOTAL_ESTRELLAS else ROJO)
            pantalla.blit(superficie, superficie.get_rect(center=(ANCHO // 2, ALTO // 2 - 15)))
            reinicio = fuente.render("Pulsa R para volver a jugar", True, BLANCO)
            pantalla.blit(reinicio, reinicio.get_rect(center=(ANCHO // 2, ALTO // 2 + 25)))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
