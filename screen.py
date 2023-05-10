import pygame
from pygame.locals import *

width = 1080
height = 720
fl_height = 450

class Screen:

    def __screen__():
        screen = pygame.display.set_mode((width, height))
        bg = pygame.image.load("images/Background.png")
        fl = pygame.image.load("images/Floor.png")
        screen.blit(bg,(0,0))
        screen.blit(fl, (0, fl_height))
