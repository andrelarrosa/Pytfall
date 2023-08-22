# self.sprites = []
# self.sprites.append(pygame.image.load('Sprites/Player/Idle/1.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/1.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/2.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/3.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/4.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/5.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/4.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/3.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/2.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/1.png'))
# pylint: disable=pointless-statement
import pygame
import os
from gameObject import GameObject, ObjectEnum
from enum import Enum


class ObjectState(Enum):
    IDLELEFT = 'IdleLeft'
    RUNNINGLEFT = 'RunningLeft'
    RUNNING = 'Running'
    IDLE = 'Idle'


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.animationIndex = 0
        self.animations = {}
        self.atual = 0
        self.load()
        self.image = self.animations['Idle'][0]
        self.rect = self.image.get_rect()

    def changeSprite(self, kind, index=None):
        if index is None:
            index = self.animationIndex

        self.image = self.animations[kind][index]
        self.rect = self.image.get_rect()
        self.rect.center = (self.image.get_width() / 2,
                            self.image.get_height() / 2)

    def load(self):
        if os.path.exists('Sprites/Player/'):
            animationNames = ['Climbing', 'Idle', 'IdleLeft', 'Jumping', 'Running', 'RunningLeft']
            for name in animationNames:
                if os.path.exists('Sprites/Player/{}'.format(name)):
                    (path, dirs, files) = \
                        os.walk('Sprites/Player/{}'.format(name)).__next__()
                    self.animations[name] = []
                    bufferArray = []

                    for i in files:
                        if i.endswith('.png'):
                            bufferArray.append(pygame.image.load('Sprites/Player/{}/{}'.format(name,i)))
                    self.animations[name] = bufferArray


class Player(GameObject):

    def __init__(self, x: int, y: int, width: int, height: int, vel_x: float, vel_y: float, is_gravity: bool = False, object_type=ObjectEnum):
        super().__init__(x, y, width, height, vel_x, vel_y, is_gravity, object_type)
        self.sprite = PlayerSprite()
        self.updateHitBox()
        self.animations = {}
        self.state = ObjectState.IDLE
        self.stateRunning = 0
        self.stateRunningDt = 0

    def changeState(self, newState):
        if(self.state == ObjectState.IDLE):
            if (newState == ObjectState.RUNNING):
                self.stateRunningDt = 0
                self.stateRunning = 0
                self.sprite.changeSprite(ObjectState.RUNNING.value, 0)

            elif (newState == ObjectState.RUNNINGLEFT):
                self.stateRunningDt = 0
                self.stateRunning = 0
                self.sprite.changeSprite(ObjectState.RUNNINGLEFT.value, 0)

        elif(self.state == ObjectState.RUNNING):
            if (newState == ObjectState.IDLE):
                self.sprite.changeSprite(ObjectState.IDLE.value, 0)


        elif(self.state == ObjectState.RUNNINGLEFT):
            if (newState == ObjectState.IDLELEFT):
                self.sprite.changeSprite(ObjectState.IDLELEFT.value, 0)

        elif (self.state == ObjectState.IDLELEFT):
            if (newState == ObjectState.RUNNING):
                self.stateRunningDt = 0
                self.stateRunning = 0
                self.sprite.changeSprite(ObjectState.RUNNING.value, 0)

            elif (newState == ObjectState.RUNNINGLEFT):
                self.stateRunningDt = 0
                self.stateRunning = 0
                self.sprite.changeSprite(ObjectState.RUNNINGLEFT.value, 0)

        self.state = newState
        self.updateHitBox()


    def key_down(self, key):
        if key == pygame.K_RIGHT:
            self.vel_x = 500.0
            self.changeState(ObjectState.RUNNING)
            self.stateRunning = 0
        if key == pygame.K_LEFT:
            self.vel_x = -500.0
            self.changeState(ObjectState.RUNNINGLEFT)
            self.stateRunning = 0
        if key == pygame.K_UP:
            if self.is_collided_platform:
                self.vel_y = -1000.0

    def key_up(self, key):
        if key == pygame.K_RIGHT:
            self.vel_x = 0.0
            self.changeState(ObjectState.IDLE)
        if key == pygame.K_LEFT:
            self.vel_x = 0.0
            self.changeState(ObjectState.IDLELEFT)

    def renderObjects(self, screen, dt):
        screen.blit(self.sprite.image, (self.x, self.y))

        if(self.state == ObjectState.RUNNING):
            self.stateRunningDt += dt

            if(self.stateRunningDt >= 0.05):
                self.stateRunning += 1

                if(self.stateRunning > 4):
                    self.stateRunning = 0

                self.stateRunningDt = 0
                self.sprite.changeSprite(ObjectState.RUNNING.value, self.stateRunning)

        elif(self.state == ObjectState.RUNNINGLEFT):
            self.stateRunningDt += dt

            if(self.stateRunningDt >= 0.05):
                self.stateRunning += 1

                if(self.stateRunning > 4):
                    self.stateRunning = 0

                self.stateRunningDt = 0
                self.sprite.changeSprite(ObjectState.RUNNINGLEFT.value, self.stateRunning)




    def updateHitBox(self):
        self.width = self.sprite.image.get_width()
        self.height = self.sprite.image.get_height()
