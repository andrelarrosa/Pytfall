import pygame
import os
from gameObject import GameObject, ObjectEnum
from enum import Enum


class ObjectState(Enum):
    RUNNING = 'Running'
    IDLE = 'Idle'


class PitSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animationIndex = 6
        self.animations = {}
        self.atual = 6
        self.load()
        self.image = self.animations['Running'][5]
        self.rect = self.image.get_rect()

    def changeSprite(self, kind, index=None):
        if index is None:
            index = self.animationIndex

        self.image = self.animations[kind][index]
        self.rect = self.image.get_rect()
        self.rect.center = (self.image.get_width() / 2,
                            self.image.get_height() / 2)

    def load(self):
        if os.path.exists('Sprites/Environment/Pit/'):
            animationNames = ['Running']
            for name in animationNames:
                if os.path.exists('Sprites/Environment/Pit/'):
                    (path, dir, files) = os.walk(
                        'Sprites/Environment/Pit/').__next__()
                    bufferArray = []
                    for i in files:
                        if i.endswith('.png'):
                            bufferArray.append(pygame.image.load(
                                'Sprites/Environment/Pit/{}'.format(i)))
                    self.animations[name] = bufferArray
#


class Pit(GameObject):

    def __init__(self, x: int, y: int, width: int, height: int, vel_x: float, vel_y: float, is_gravity: bool = False, object_type=ObjectEnum):
        super().__init__(x, y, width, height, vel_x, vel_y, is_gravity, object_type)
        self.sprite = PitSprite()
        self.updateHitBox()
        self.animations = {}
        self.state = ObjectState.IDLE
        self.stateRunning = 0
        self.stateRunningDt = 0

    def changeState(self, newState):
        if (self.state == ObjectState.IDLE):
            if (newState == ObjectState.RUNNING):
                self.stateRunningDt = 0
                self.stateRunning = 0
                self.sprite.changeSprite(ObjectState.RUNNING.value, 0)

        self.state = newState
        self.updateHitBox()

    def goLeft(self):
        self.vel_x = -350.0
        self.changeState(ObjectState.RUNNING)

    def renderObjects(self, screen, dt):
        screen.blit(self.sprite.image, (self.x, self.y))

        if (self.x < -1 * self.width):
            self.x = 1080

        if (self.state == ObjectState.RUNNING):
            self.stateRunningDt += dt

            if (self.stateRunningDt >= 0.5):
                self.stateRunning += 1

                if (self.stateRunning > 1):
                    self.stateRunning = 0

                self.stateRunningDt = 0
                self.sprite.changeSprite(
                    ObjectState.RUNNING.value, self.stateRunning)

    def updateHitBox(self):
        self.width = self.sprite.image.get_width()
        self.height = self.sprite.image.get_height()
