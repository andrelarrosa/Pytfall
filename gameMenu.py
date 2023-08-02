import pygame
from pygame.locals import *
from gameScreen import GameScreen


class GameMenu:

    def __init__(self):
        pygame.init()
        self.width = 1080
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.backgroundMenu = pygame.image.load('Sprites/Menu.png')
        self.buttonPlay = pygame.image.load('Sprites/Menu/Play.png')
        self.buttonQuit = pygame.image.load('Sprites/Menu/Quit.png')
        self.soundEnter = pygame.mixer.Sound('Sounds/boom.wav')
        self.soundWhoosh = pygame.mixer.Sound('Sounds/whoosh.wav')
        pygame.mixer.music.load('Sounds/metallica.wav')
        pygame.mixer.music.play(-1)
        self.initialized = False
        self.gameScreen = GameScreen()
        self.running = True


    def telaMenu(self):
        self.screen.blit(self.backgroundMenu, (0, 0))
        self.screen.blit(self.buttonPlay, (467, 417))
        self.screen.blit(self.buttonQuit, (466, 576))

    def initGameMenu(self):
        while self.running:
            self.telaMenu()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p and not self.initialized:
                    self.soundWhoosh.play()
                    self.initialized = True
                    self.gameScreen.initGame()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    self.running = False
