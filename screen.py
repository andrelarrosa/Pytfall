import pygame
from pygame.locals import *

class Screen:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pytfall')
        self.gravity = 9.8
        self.width = 1080
        self.height = 720
        self.fl_height = 450
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load("images/Background.png")
        self.fl = pygame.image.load("images/Floor.png")
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.fl, (0, self.fl_height))
        self.running = True

    def desenharTela(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.fl, (0, self.fl_height))
        pygame.display.flip()
    
    def aplicarGravidade(self):
        # Limitar a atualização da tela para 60 quadros por segundo
        time = pygame.time.Clock().tick(60)
        # Aplicação da gravidade
        vel_y = 0.5 * self.gravity * time**2


    def iniciarTela(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.aplicarGravidade()
            self.desenharTela()
        pygame.quit()




   