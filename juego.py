import pygame
import math
import pygame
import math
import pygame
import math
import pygame
import math
import math
import pygame
import pygame
import math
import pygame
import math
import pygame
import math
import pygame
import math
import pygame
import math
import pygame
import math
import pygame
import math

# Definir el tamaño de la pantalla
screen_width = 800
screen_height = 600

# Definir los colores con menor intensidad
RED = (50, 0, 0)
GREEN = (0, 50, 0)

# Definir las propiedades del círculo
radius = min(screen_width, screen_height) // 10
center_x = screen_width // 2
center_y = screen_height // 2
angle = 0
angular_speed = 0.1

# Inicializar Pygame
pygame.init()

# Crear la ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego")

# Función para dibujar el círculo en la pantalla
def draw_circle(color):
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)

    # Dibujar la cara de miedo
    eye_radius = radius // 5
    eye_x_offset = radius // 3
    eye_y_offset = radius // 3
    mouth_width = radius // 2
    mouth_height = radius // 4

    # Dibujar los ojos
    pygame.draw.circle(screen, (0, 0, 0), (int(x - eye_x_offset), int(y - eye_y_offset)), eye_radius)
    pygame.draw.circle(screen, (0, 0, 0), (int(x + eye_x_offset), int(y - eye_y_offset)), eye_radius)

    # Dibujar la boca
    pygame.draw.rect(screen, (0, 0, 0), (int(x - mouth_width/2), int(y + eye_y_offset), mouth_width, mouth_height))

# Función para dibujar el botón en la pantalla
def draw_button():
    button_width = screen_width // 4
    button_height = screen_height // 12
    button_x = (screen_width - button_width) // 2
    button_y = screen_height - button_height - screen_height // 30
    pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))

# Bucle principal del juego
running = True
button_clicked = False
while running:
    # Actualizar la posición del círculo
    angle += angular_speed

    # Dibujar el círculo
    if button_clicked:
        draw_circle(GREEN)
    else:
        draw_circle(RED)

    # Dibujar el botón
    draw_button()

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Definir el tamaño de la pantalla
screen_width = 800
screen_height = 600

# Definir los colores con menor intensidad
RED = (100, 0, 0)
GREEN = (0, 100, 0)
angle = 0
angular_speed = 0.1

# Inicializar Pygame
pygame.init()

# Crear la ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego")

# Función para dibujar el círculo en la pantalla
def draw_circle(color):
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)

# Función para dibujar el botón en la pantalla
def draw_button():
    button_width = screen_width // 4
    button_height = screen_height // 12
    button_x = (screen_width - button_width) // 2
    button_y = screen_height - button_height - screen_height // 30
    pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))

# Bucle principal del juego
running = True
button_clicked = False
while running:
    # Actualizar la posición del círculo
    angle += angular_speed

    # Dibujar el círculo
    if button_clicked:
        draw_circle(GREEN)
    else:
        draw_circle(RED)


    # Definir el tamaño de la pantalla
    screen_width = 800
    screen_height = 600

    # Definir los colores
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)

    # Definir las propiedades del círculo
    radius = min(screen_width, screen_height) // 10
    center_x = screen_width // 2
    center_y = screen_height // 2
    angle = 0
    angular_speed = 0.1

    # Inicializar Pygame
    pygame.init()

    # Crear la ventana
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Juego")

    # Función para dibujar el círculo en la pantalla
    def draw_circle(color):
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        pygame.draw.circle(screen, color, (int(x), int(y)), radius)

        # Dibujar la cara feliz
        pygame.draw.circle(screen, YELLOW, (int(x - radius // 4), int(y - radius // 4)), radius // 4)  # Ojo izquierdo
        pygame.draw.circle(screen, YELLOW, (int(x + radius // 4), int(y - radius // 4)), radius // 4)  # Ojo derecho
        pygame.draw.arc(screen, YELLOW, (int(x - radius // 2), int(y - radius // 2), radius, radius), math.pi, 2 * math.pi, 3)  # Sonrisa

    # Función para dibujar el botón en la pantalla
    def draw_button():
        button_width = screen_width // 4
        button_height = screen_height // 12
        button_x = (screen_width - button_width) // 2
        button_y = screen_height - button_height - screen_height // 30
        pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))

    # Bucle principal del juego
    running = True
    button_clicked = False
    while running:
        # Actualizar la posición del círculo
        angle += angular_speed

        # Dibujar el círculo
        if button_clicked:
            draw_circle(GREEN)
        else:
            draw_circle(RED)

        # Dibujar el botón
        draw_button()

        # Actualizar la pantalla
        pygame.display.flip()

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
                if button_rect.collidepoint(mouse_pos):
                    button_clicked = not button_clicked
            elif event.type == pygame.QUIT:
                running = False

# Definir el tamaño de la pantalla
screen_width = 800
screen_height = 600

# Definir los colores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Definir las propiedades del círculo
radius = min(screen_width, screen_height) // 10
center_x = screen_width // 2
center_y = screen_height // 2
angle = 0
angular_speed = 0.1

# Inicializar Pygame
pygame.init()

# Crear la ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego")

# Función para dibujar el círculo en la pantalla
def draw_circle(color):
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)

    # Dibujar la cara feliz
    pygame.draw.circle(screen, YELLOW, (int(x - radius // 4), int(y - radius // 4)), radius // 4)  # Ojo izquierdo
    pygame.draw.circle(screen, YELLOW, (int(x + radius // 4), int(y - radius // 4)), radius // 4)  # Ojo derecho
    pygame.draw.arc(screen, YELLOW, (int(x - radius // 2), int(y - radius // 2), radius, radius), math.pi, 2 * math.pi, 3)  # Sonrisa

# Función para dibujar el botón en la pantalla
def draw_button():
    button_width = screen_width // 4
    button_height = screen_height // 12
    button_x = (screen_width - button_width) // 2
    button_y = screen_height - button_height - screen_height // 30
    pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))

# Bucle principal del juego
running = True
button_clicked = False
while running:
    # Actualizar la posición del círculo
    angle += angular_speed

    # Dibujar el círculo
    if button_clicked:
        draw_circle(GREEN)
    else:
        draw_circle(RED)

    # Dibujar el botón
    draw_button()

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            if button_rect.collidepoint(mouse_pos):
                button_clicked = not button_clicked
        elif event.type == pygame.QUIT:
            running = False

# Definir el tamaño de la pantalla
screen_width = 800
screen_height = 600

# Definir los colores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Definir las propiedades del círculo
radius = min(screen_width, screen_height) // 10
center_x = screen_width // 2
center_y = screen_height // 2
angle = 0
angular_speed = 0.1

# Inicializar Pygame
pygame.init()

# Crear la ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego")

# Función para dibujar el círculo en la pantalla
def draw_circle(color):
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)

    # Dibujar la cara feliz
    pygame.draw.circle(screen, YELLOW, (int(x - radius // 4), int(y - radius // 4)), radius // 4)  # Ojo izquierdo
    pygame.draw.circle(screen, YELLOW, (int(x + radius // 4), int(y - radius // 4)), radius // 4)  # Ojo derecho
    pygame.draw.arc(screen, YELLOW, (int(x - radius // 2), int(y - radius // 2), radius, radius), math.pi, 2 * math.pi, 3)  # Sonrisa

# Función para dibujar el botón en la pantalla
def draw_button():
    button_width = screen_width // 4
    button_height = screen_height // 12
    button_x = (screen_width - button_width) // 2
    button_y = screen_height - button_height - screen_height // 30
    pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))

# Bucle principal del juego
running = True
button_clicked = False
while running:
    # Actualizar la posición del círculo
    angle += angular_speed

    # Dibujar el fondo
    screen.fill(BLUE)

    # Dibujar el círculo
    if button_clicked:
        draw_circle(GREEN)
    else:
        draw_circle(RED)

    # Dibujar el botón
    draw_button()

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            if button_rect.collidepoint(mouse_pos):
                button_clicked = not button_clicked
        elif event.type == pygame.QUIT:
            running = False

# Definir el tamaño de la pantalla
screen_width = 800
screen_height = 600

# Definir los colores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Definir las propiedades del círculo
radius = min(screen_width, screen_height) // 10
center_x = screen_width // 2
center_y = screen_height // 2
angle = 0
angular_speed = 0.1

# Inicializar Pygame
pygame.init()

# Crear la ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego")

# Función para dibujar el círculo en la pantalla
def draw_circle(color):
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)

    # Dibujar la cara feliz
    pygame.draw.circle(screen, YELLOW, (int(x - radius // 4), int(y - radius // 4)), radius // 4)  # Ojo izquierdo
    pygame.draw.circle(screen, YELLOW, (int(x + radius // 4), int(y - radius // 4)), radius // 4)  # Ojo derecho
    pygame.draw.arc(screen, YELLOW, (int(x - radius // 2), int(y - radius // 2), radius, radius), math.pi, 2 * math.pi, 3)  # Sonrisa

# Función para dibujar el botón en la pantalla
def draw_button():
    button_width = screen_width // 4
    button_height = screen_height // 12
    button_x = (screen_width - button_width) // 2
    button_y = screen_height - button_height - screen_height // 30
    pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))

# Bucle principal del juego
running = True
button_clicked = False
while running:
    # Actualizar la posición del círculo
    angle += angular_speed

    # Dibujar el fondo
    screen.fill(BLUE)

    # Dibujar el círculo
    if button_clicked:
        draw_circle(GREEN)
    else:
        draw_circle(RED)

    # Dibujar el botón
    draw_button()

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            if button_rect.collidepoint(mouse_pos):
                button_clicked = not button_clicked
        elif event.type == pygame.QUIT:
            running = False
# Función para dibujar el botón en la parte superior de la pantalla
def draw_button():
    button_width = screen_width // 4
    button_height = screen_height // 12
    button_x = (screen_width - button_width) // 2
    button_y = screen_height // 30
    pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))

# Definir el tamaño de la pantalla
screen_width = 800
screen_height = 600

# Definir las propiedades del círculo
radius = min(screen_width, screen_height) // 10
center_x = screen_width // 2
center_y = screen_height // 2
angle = 0
angular_speed = 0.1

# Definir los colores del arcoiris
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# Inicializar Pygame
pygame.init()

# Crear la ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego")

# Función para dibujar el círculo en la pantalla
def draw_circle(color):
    pygame.draw.circle(screen, color, (center_x, center_y), radius)

# Función para dibujar el botón en la pantalla
def draw_button():
    button_width = screen_width // 4
    button_height = screen_height // 12
    button_x = (screen_width - button_width) // 2
    button_y = screen_height - button_height - screen_height // 30
    pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))

# Bucle principal del juego
running = True
button_clicked = False
color_index = 0
while running:
    # Actualizar la posición del círculo
    angle += angular_speed

    # Dibujar el fondo del arcoiris
    screen.fill(colors[color_index])

    # Dibujar el círculo
    if button_clicked:
        draw_circle(GREEN)
    else:
        draw_circle(RED)

    # Dibujar el botón
    draw_button()

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            if button_rect.collidepoint(mouse_pos):
                button_clicked = not button_clicked
        elif event.type == pygame.QUIT:
            running = False

    # Cambiar el color del arcoiris
    color_index = (color_index + 1) % len(colors)
