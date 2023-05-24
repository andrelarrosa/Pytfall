import pygame
from pygame.locals import *

class Engine:
   
    def __init__(self, screen_width, screen_height):
        self.x = 100
        self.y = 100
        self.width = 50
        self.height = 50
        self.vel_x = 0
        self.vel_y = 0
        self.platform_width = 800
        self.platform_height = 20
        self.platform_x = screen_width // 2 - self.platform_width // 2
        self.platform_y = screen_height - self.platform_height - 10

    def atualizarPosicaoObjeto(self):
        self.x += vel_x
        self.y += vel_y

    def colisaoPlataforma(self):
        # Colisão com a plataforma
        if self.y + self.height >= self.platform_y and self.vel_y >= 0:
            if self.x + self.width >= self.platform_x and self.x <= self.platform_x + self.platform_width:
                self.vel_y = 0
                self.y = self.platform_y - self.height

    def colisaoBorda(self):
        # Colisão com as bordas da tela
        if self.x <= 0 or self.x + self.width >= self.screen_width:
            self.vel_x *= -1
