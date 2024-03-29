import pygame
from enum import Enum

class ObjectEnum(Enum):
    PLAYER = 1
    PLATFORM = 2
    GHOST = 3   
    BARREL = 4
    PIT = 5


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

    def renderObjects(self, screen, dt):
        pass

    def pre_physics(self):
        self.is_collided_platform = False
        