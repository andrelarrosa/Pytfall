import pygame
from pygame.locals import *
from gameScreen import GameScreen

class GameMenu:

    def __init__(self):
        pygame.init()
        self.width = 1080
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.load_assets()
        pygame.mixer.music.load('Sounds/metallica.wav')
        pygame.mixer.music.play(-1)
        self.initialized = False
        self.gameScreen = GameScreen()
        self.running = True

    def load_assets(self):
        self.backgroundMenu = pygame.image.load('Sprites/Menu.png')
        self.buttonPlay = pygame.image.load('Sprites/Menu/Play.png')
        self.buttonQuit = pygame.image.load('Sprites/Menu/Quit.png')
        self.soundEnter = pygame.mixer.Sound('Sounds/boom.wav')
        self.soundWhoosh = pygame.mixer.Sound('Sounds/whoosh.wav')

    def draw_menu(self):
        self.screen.blit(self.backgroundMenu, (0, 0))
        self.screen.blit(self.buttonPlay, (467, 417))
        self.screen.blit(self.buttonQuit, (466, 576))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and not self.initialized:
                    self.soundWhoosh.play()
                    self.initialized = True
                    self.screen.blit(self.backgroundMenu, (0, 0))
                    self.gameScreen.initGame()
                elif event.key == pygame.K_q:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    self.running = False

    def run(self):
        while self.running:
            self.draw_menu()
            pygame.display.flip()
            self.handle_events()


