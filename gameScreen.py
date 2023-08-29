import pygame
from pygame.locals import *
from gameObject import GameObject, ObjectEnum
from platform import Platform
from player import Player
from ghost import Ghost
from barrel import Barrel
from pit import Pit
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
        self.level = 0
        self.dt = 0
        self.pit = None
        self.player = None
        self.ghost = None
        self.barrel = None
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

    def collidedWithGhost(self, obj_ghost: Ghost, obj: Player):
        exit()

    def objectsCollided(self, obj: GameObject, obj_2: GameObject):
        if (obj.object_type == ObjectEnum.PLATFORM ):
            self.collidedWithPlatform(obj, obj_2)
        elif (obj_2.object_type == ObjectEnum.PLATFORM):
            self.collidedWithPlatform(obj_2, obj)
        elif (obj.object_type == ObjectEnum.GHOST and obj_2.object_type == ObjectEnum.PLAYER):
            self.collidedWithGhost(obj, obj_2)
        elif (obj.object_type == ObjectEnum.PLAYER and obj_2.object_type == ObjectEnum.GHOST):
            self.collidedWithGhost(obj_2, obj)
        elif (obj.object_type == ObjectEnum.BARREL and obj_2.object_type == ObjectEnum.PLAYER):
            self.collidedWithGhost(obj, obj_2)
        elif (obj.object_type == ObjectEnum.PLAYER and obj_2.object_type == ObjectEnum.BARREL):
            self.collidedWithGhost(obj_2, obj)
        elif (obj.object_type == ObjectEnum.PIT and obj_2.object_type == ObjectEnum.PLAYER):
            self.collidedWithGhost(obj_2, obj)
        elif (obj.object_type == ObjectEnum.PLAYER and obj_2.object_type == ObjectEnum.PIT):
            self.collidedWithGhost(obj, obj_2)

    def collision(self):
        for i in range(0, len(self.objectList) - 1):
            for j in range(i+1, len(self.objectList)):
                if (self.objectsInCollision(self.objectList[j], self.objectList[i])):
                    self.objectsCollided(self.objectList[j], self.objectList[i])

    def adicionarObjeto(self, obj: GameObject):
        self.objectList.append(obj)

    def destruirObjeto(self, obj: GameObject):
        self.objectList.remove(obj)

    def renderObjects(self, dt):
        self.desenharTela()
        for obj in self.objectList:
            obj.renderObjects(self.screen, dt)

        pygame.display.flip()

    def initGame(self, level):
        self.level = level
        if(level == 0):
            self.platform = Platform(0, 485, 1080, 20, 0, 0, False,  ObjectEnum.PLATFORM)
            self.player = Player(10, 435, 50, 50, 0, 0, True, ObjectEnum.PLAYER)
            self.adicionarObjeto(self.platform)
            self.adicionarObjeto(self.player)

        elif(level == 1):
            self.player.x = -20
            self.barrel = Barrel(1080, 435, 50, 50, 0, 0, True, ObjectEnum.BARREL)
            self.adicionarObjeto(self.barrel)
            self.barrel.goLeft()

        elif(level == 2):
            self.destruirObjeto(self.barrel)
            self.player.x = -20
            self.ghost = Ghost(1080, 435, 50, 50, 0, 0, True, ObjectEnum.GHOST)
            self.adicionarObjeto(self.ghost)
            self.ghost.goLeft()

        elif(level == 3):
            self.destruirObjeto(self.ghost)
            self.player.x = -20
            self.pit = Pit(320, 485, 50, 50, 0, 0, True, ObjectEnum.PIT)
            self.adicionarObjeto(self.pit)


        self.lacoPrincipal()

    def checkAlterLevel(self):
        if (self.player.x >= 1080):
            self.level += 1
            self.initGame(self.level)



    def lacoPrincipal(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.player.key_down(event.key)
                    if event.key == pygame.K_q:
                        pygame.mixer.music.stop()
                        pygame.quit()
                        self.running = False

                elif event.type == pygame.KEYUP:
                    self.player.key_up(event.key)

                elif event.type == QUIT:
                    exit()

            self.physics(self.dt)
            self.collision()
            self.checkAlterLevel()
            self.renderObjects(self.dt)
            self.dt = pygame.time.Clock().tick(60)/1000.0
        pygame.quit()



