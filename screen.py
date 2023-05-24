import pygame
from pygame.locals import *

# class Screen:

#     def __screen__():
#         width = 1080
#         height = 720
#         fl_height = 450
#         screen = pygame.display.set_mode((width, height))
#         bg = pygame.image.load("images/Background.png")
#         fl = pygame.image.load("images/Floor.png")
#         screen.blit(bg,(0,0))
#         screen.blit(fl, (0, fl_height))

#     def aplicarGravidade():
#         gravity = 9.8
#         vel_y = 0
#         vel_x = 0
#         x = 100
#         y = 100
#         # Limitar a atualização da tela para 60 quadros por segundo
#         time = pygame.time.Clock().tick()
#         # Aplicação da gravidade
#         #0 = 0 + vel_y - 1/2 * gravity * t^2
#         vel_y = 0.5 * gravity * time**2
#         # Atualização da posição do objeto
#         x += vel_x
#         y += vel_y
