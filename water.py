import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 420, 280

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SCALED|pygame.FULLSCREEN)
pygame.display.set_caption("Efecto de Ondas en una Lista de Coordenadas")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)




# Función para generar el efecto de ondas en una lista de coordenadas
def generar_efecto_ondas(coordinates, amplitude, frequency, damping):
    wave = 0

    displacement = [0] * len(coordinates)
    clock = pygame.time.Clock()
    running = True
    rect = pygame.Rect(100,0,40,40)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar el desplazamiento de cada coordenada

        for i in range(len(coordinates)):
            coordinates[i][1] = int(math.sin(i+ wave)*5 + 200 + math.sin(wave)*5)
        wave += 0.05

        screen.fill(WHITE)
        rect.centery =  coordinates[len(coordinates)//2][1]
        rect.centerx = pygame.mouse.get_pos()[0]
        pygame.draw.rect(screen,(255,0,0),rect,2)
        lines_rect = pygame.draw.lines(screen, BLUE, False, coordinates, 2)
        pygame.draw.rect(screen,(0,200,200),lines_rect,2)
        # pygame.draw.lines(screen, (255,0,0), False, coordinates, 1)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()




# Lista de coordenadas (x, y)
coordinates2 = [(100, 100), (200, 200), (300, 300), (400, 400), (500, 500)]

coordinates = [[i,400+math.sin(i)*5] for i in range(0,800,7)]





# Parámetros para la simulación de ondas
amplitude = 20  # Amplitud de las ondas
frequency = 10  # Frecuencia de las ondas
damping = 0.1  # Factor de amortiguamiento

# Llamar a la función para generar el efecto de ondas
generar_efecto_ondas(coordinates, amplitude, frequency, damping)
