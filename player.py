# self.sprites = []
# self.sprites.append(pygame.image.load('Sprites/Player/Idle/1.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/1.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/2.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/3.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/4.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/5.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/4.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/3.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/2.png'))
# self.sprites.append(pygame.image.load('Sprites/Player/Running/1.png'))
# pylint: disable=pointless-statement
import pygame
import os
from gameObject import GameObject, ObjectEnum

        

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.animationIndex = 0
        self.animations = {}
        self.atual = 0
        self.load()
        self.image = self.animations['Idle'][0]
        self.rect = self.image.get_rect()

    def changeSprite(self, kind, index=None):
        if index is None:
            index = self.animationIndex

        self.image = self.animations[kind][index]
        self.rect = self.image.get_rect()
        self.rect.center = (self.image.get_width() / 2,
                            self.image.get_height() / 2)
    
    def load(self):
        if os.path.exists('Sprites/Player/'):
            animationNames = ['Climbing', 'Idle', 'Jumping', 'Running']
            for name in animationNames:
                if os.path.exists('Sprites/Player/{}'.format(name)):
                    (path, dirs, files) = \
                        os.walk('Sprites/Player/{}'.format(name)).__next__()
                    self.animations[name] = []
                    bufferArray = []

                    for i in files:
                        if i.endswith('.png'):
                            bufferArray.append(pygame.image.load('Sprites/Player/{}/{}'.format(name,i)))
                    self.animations[name] = bufferArray

    


    def updateSprite(self):
        self.atual = self.atual + 0.06  
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))

                    
#código que pega o evento do teclado tem que ficar aqui

class Player(GameObject):

    def __init__(self, x: int, y: int, width: int, height: int, vel_x: float, vel_y: float, is_gravity: bool = False, object_type=ObjectEnum):
        super().__init__(x, y, width, height, vel_x, vel_y, is_gravity, object_type)
        self.sprite = PlayerSprite()

    def renderObjects(self, screen):
        print("Chegou")
        screen.blit(self.sprite.image, (100, 200))
