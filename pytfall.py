import pygame
from gameScreen import GameScreen
from pygame.locals import *
from engine import *
from gameObject import GameObject

screen = GameScreen()
plataforma = GameObject(10, 435, 50, 50, 0, 0)
screen.initGame()
screen.lacoPrincipal()

