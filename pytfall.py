import pygame
# from screen import *
from pygame.locals import *
from engine import *

pygame.init()


class Screen:

    def __screen__():
        width = 1080
        height = 720
        fl_height = 450
        screen = pygame.display.set_mode((width, height))
        bg = pygame.image.load("images/Background.png")
        fl = pygame.image.load("images/Floor.png")
        screen.blit(bg, (0, 0))
        screen.blit(fl, (0, fl_height))

    def aplicarGravidade():
        global vel_y
        global y
        global gravity
        global vel_x
        global x
        gravity = 9.8
        vel_y = 0
        vel_x = 0
        x = 100
        y = 100
        # Limitar a atualização da tela para 60 quadros por segundo
        time = pygame.time.Clock().tick(60)
        # Aplicação da gravidade
        # 0 = 0 + vel_y - 1/2 * gravity * t^2
        vel_y = 0.5 * gravity * time**2
        # Atualização da posição do objeto
        x += vel_x
        y += vel_y

Screen.__screen__()
pygame.display.set_caption('Pytfall')

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Exemplo de Física com Pygame")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)



# Parâmetros do objeto em movimento
x = 100
y = 100
width = 50
height = 50
vel_x = 0
vel_y = 10
gravity = 0.5

# Plataforma
platform_width = 800
platform_height = 20
platform_x = screen_width // 2 - platform_width // 2
platform_y = screen_height - platform_height - 10




# Função para desenhar o objeto e a plataforma na tela
def draw_objects():
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.draw.rect(screen, RED, (platform_x, platform_y, platform_width, platform_height))
    pygame.display.update()

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Screen.aplicarGravidade()

    # # Atualização da posição do objeto
    # x += vel_x
    # y += vel_y

    # Colisão com a plataforma
    if y + height >= platform_y and vel_y >= 0:
        if x + width >= platform_x and x <= platform_x + platform_width:
            vel_y = 0
            y = platform_y - height

    # Colisão com as bordas da tela
    if x <= 0 or x + width >= screen_width:
        vel_x *= -1

    # Desenhar os objetos na tela
    draw_objects()

    pygame.time.Clock().tick(60)

# Encerrar o Pygame
pygame.quit()