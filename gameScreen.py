import pygame
from pygame.locals import *
from gameObject import GameObject, ObjectEnum
from player import Player
from engine import Engine



class GameScreen:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pytfall')
        self.gravity = 3000.0
        self.width = 1080
        self.height = 720
        self.fl_height = 450
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load("Sprites/Background.png")
        self.fl = pygame.image.load("Sprites/Environment/Floor.png")
        self.objectList = []
        self.dt = 0
        self.player = None
        self.sprite = None
        self.platform = None
        self.engine = None
        self.running = True

    def desenharTela(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.fl, (0, self.fl_height))
    
    def physics(self, dt):
        for obj in self.objectList:
            obj.pre_physics()
        for obj in self.objectList:
            if obj.is_gravity:
                obj.vel_y += self.gravity * dt
            obj.x = obj.x + obj.vel_x * dt
            obj.y = obj.y + obj.vel_y * dt

    def objectsInCollision(self, obj: GameObject, obj_2: GameObject):
        return (abs((obj.x + obj.width/2.0) - (obj_2.x + obj_2.width/2.0)) < ((obj.width + obj_2.width) / 2.0) and abs((obj.y + obj.height/2.0) - (obj_2.y + obj_2.height/2.0)) < ((obj.height + obj_2.height) / 2.0))
    
    def collidedWithPlatform(self, obj_platform: GameObject, obj: GameObject):
        if obj.y + obj.height >= obj_platform.y:
            obj.vel_y = 0
            obj.y = obj_platform.y - obj.height
            obj.is_collided_platform = True

    def objectsCollided(self, obj: GameObject, obj_2: GameObject):
        if (obj.object_type == ObjectEnum.PLATFORM ):
            self.collidedWithPlatform(obj, obj_2)
        elif (obj_2.object_type == ObjectEnum.PLATFORM):
            self.collidedWithPlatform(obj_2, obj)

    def collision(self):
        for i in range(0, len(self.objectList) - 1):
            for j in range(i+1, len(self.objectList)):
                if (self.objectsInCollision(self.objectList[j], self.objectList[i])):
                    self.objectsCollided(self.objectList[j], self.objectList[i])

    def adicionarObjeto(self, obj: GameObject):
        self.objectList.append(obj)

    def renderObjects(self):
        self.desenharTela()
        for obj in self.objectList:
            obj.renderObjects(self.screen)
        
        pygame.display.flip()

    def initGame(self):
        self.engine = Engine()
        self.platform = GameObject(0, 485, 1080, 20, 0, 0, False,  ObjectEnum.PLATFORM)
        self.player = Player(10, 435, 50, 50, 0, 0, True, ObjectEnum.PLAYER)
        self.adicionarObjeto(self.platform)
        self.adicionarObjeto(self.player)
        self.lacoPrincipal()
        
        

    def lacoPrincipal(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.vel_x = 500.0
                    if event.key == pygame.K_LEFT:
                        self.player.vel_x = -500.0
                    if event.key == pygame.K_UP:
                        if self.player.is_collided_platform:
                            self.player.vel_y = -850.0
                    if event.key == pygame.K_q:
                        pygame.mixer.music.stop()
                        pygame.quit()
                        self.running = False

                elif event.type == pygame.KEYUP:    
                    if event.key == pygame.K_RIGHT:
                        self.player.vel_x = 0.0
                    if event.key == pygame.K_LEFT:
                        self.player.vel_x = 0.0 
                
                elif event.type == QUIT:
                    exit()    
                     
            self.physics(self.dt)
            self.collision()
            self.renderObjects()
            
            self.dt = pygame.time.Clock().tick(60)/1000.0
        pygame.quit()



   