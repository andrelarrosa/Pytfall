import pygame
from screen import Screen
from pygame.locals import *
from engine import *
from gameObject import GameObject


screen = Screen()
objeto = GameObject(100, 100, 50, 50, 0, 0)
screen.adicionarObjeto(objeto)
screen.iniciarTela()