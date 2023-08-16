import pygame
from enum import Enum
from gameObject import GameObject, ObjectEnum

class Platform(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int, vel_x: float, vel_y: float, is_gravity: bool = False, object_type: ObjectEnum = 0):
        super().__init__(x, y, width, height, vel_x, vel_y, is_gravity, object_type)

    def renderObjects(self, screen, dt):
        # print("chegou plataforma")
        RED = (255, 0, 0)       
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
    

        