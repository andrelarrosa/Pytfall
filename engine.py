import pygame
from pygame.locals import *
from gameObject import GameObject

class Engine:
   
    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = 50
        self.height = 50
        self.vel_x = 0
        self.vel_y = 0

    def colisaoPlataforma(self, plataforma: GameObject):
        # Colisão com a plataforma
        if self.y + self.height >= plataforma.y and self.vel_y >= 0:
            if self.x + self.width >= plataforma.x and self.x <= plataforma.x + plataforma.width:
                self.vel_y = 0
                self.y = plataforma.y - self.height

    # def colisaoBorda(self):
    #     # Colisão com as bordas da tela
    #     if self.x <= 0 or self.x + self.width >= self.screen_width:
    #         self.vel_x *= -1