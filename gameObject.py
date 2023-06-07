import pygame

class GameObject:
    def __init__(self, x: int, y: int, width: int, height: int, vel_x: float, vel_y: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel_x = vel_x
        self.vel_y = vel_y

    def renderObjects(self, screen):
        RED = (255, 0, 0)
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        