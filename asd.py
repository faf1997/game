import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
window_size = (800, 600)
pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)

# Función para dibujar una matriz
def draw_matrix(matrix, color):
    glPushMatrix()
    glLoadIdentity()
    glColor(color)
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value == 1:
                x = col_index
                y = -row_index
                glRectf(x, y, x + 1, y - 1)
    glPopMatrix()

# Definir dos matrices de ejemplo
matrix1 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

matrix2 = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Dibujar las matrices una encima de la otra
    draw_matrix(matrix1, (1, 0, 0))  # Matriz 1 en rojo
    draw_matrix(matrix2, (0, 0, 1))  # Matriz 2 en azul

    pygame.display.flip()
    pygame.time.wait(10)
