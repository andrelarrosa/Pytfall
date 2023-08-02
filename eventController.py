import pygame
from pygame.locals import *
from gameScreen import GameScreen


class EventController:

    def __init__(self):
        pygame.init()
        self.gameScreen = GameScreen()
        self.initialized = False
        self.running = True

    def gameMenuEventController(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p and not self.initialized:
                    self.soundWhoosh.play()
                    self.initialized = True
                    self.gameScreen.initGame()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    self.running = False
