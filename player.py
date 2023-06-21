import pygame

from gameObject import GameObject, ObjectEnum

class Player(GameObject):

    def __init__(self, x: int, y: int, width: int, height: int, vel_x: float, vel_y: float, is_gravity: bool = False, object_type = ObjectEnum):
        super().__init__(x, y, width, height, vel_x, vel_y, is_gravity, object_type)
        self.hitbox = GameObject(self.x, self.y, self.width + 10, self.height+10, 0, 0, True, ObjectEnum.HITBOX)