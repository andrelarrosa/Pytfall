import pygame
from pygame.locals import *
from gameObject import GameObject
from player import Player

class GameScreen:

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
        self.objectList = []
        # self.lastTime = 0
        self.dt = 0
        self.player = None
        self.running = True

    def desenharTela(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.fl, (0, self.fl_height))
    
    def physics(self, dt):
        for obj in self.objectList:
            obj.x = obj.x + obj.vel_x * dt
            obj.y = obj.y + obj.vel_y * dt

    def adicionarObjeto(self, obj: GameObject):
        self.objectList.append(obj)

    def renderObjects(self):
        self.desenharTela()
        for obj in self.objectList:
            obj.renderObjects(self.screen)

        pygame.display.flip()

    def initGame(self):
        # objeto = GameObject(10, 435, 50, 50, 0, 0)
        self.player = Player(10, 435, 50, 50, 0, 0)
        self.adicionarObjeto(self.player)

    def lacoPrincipal(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.vel_x = 100.0

                elif event.type == pygame.KEYUP:    
                    if event.key == pygame.K_RIGHT:
                        self.player.vel_x = 0.0


            self.physics(self.dt)
            self.renderObjects()
            self.dt = pygame.time.Clock().tick(60)/1000.0
        pygame.quit()




   