import pygame
from enum import Enum

class ObjectEnum(Enum):
    PLAYER = 1
    PLATFORM = 2


class GameObject:
    def __init__(self, x: int, y: int, width: int, height: int, vel_x: float, vel_y: float, is_gravity: bool = False, object_type: ObjectEnum = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.is_gravity = is_gravity
        self.object_type = object_type
        self.is_collided_platform = False

    def renderObjects(self, screen):
        RED = (255, 0, 0)       
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def pre_physics(self):
        self.is_collided_platform = False
        