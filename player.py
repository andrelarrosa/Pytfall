import pygame

from gameObject import GameObject

class Player(GameObject):

    def __init__(self, x: int, y: int, width: int, height: int, vel_x: float, vel_y: float):
        super().__init__(x, y, width, height, vel_x, vel_y)
          
                    
