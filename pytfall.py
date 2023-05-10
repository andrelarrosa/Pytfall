import pygame
from screen import *
from pygame.locals import *

pygame.init()
Screen.__screen__()
pygame.display.set_caption('Pytfall')

while True:
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
   
    pygame.display.update()

