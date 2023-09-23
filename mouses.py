import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Múltiples Ratones en Pygame")

# Lista para almacenar las posiciones de los "ratones"
mouse_positions = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Simula eventos de ratón para cada "ratón"
        if event.type == pygame.MOUSEMOTION:
            mouse_positions.append(event.pos)

    # Dibuja la posición de cada "ratón"
    screen.fill((0, 0, 0))  # Limpia la pantalla
    for pos in mouse_positions:
        pygame.draw.circle(screen, (255, 0, 0), pos, 5)  # Dibuja un círculo en cada posición
    pygame.display.update()
    print(len(mouse_positions))

# Cierra Pygame
pygame.quit()
sys.exit()
