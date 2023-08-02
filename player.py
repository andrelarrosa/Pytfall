# pylint: disable=pointless-statement
import pygame

from gameObject import GameObject, ObjectEnum

class Player(GameObject):

    def __init__(self, x: int, y: int, width: int, height: int, vel_x: float, vel_y: float, is_gravity: bool = False, object_type = ObjectEnum):
        super().__init__(x, y, width, height, vel_x, vel_y, is_gravity, object_type)
        self.sprite = PlayerSprite()
    
          

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Sprites/Player/Idle/1.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/Running/1.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/Running/2.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/Running/3.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/Running/4.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/Running/5.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/Running/4.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/Running/3.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/Running/2.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/Running/1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()
    
    def updateSprite(self):
        self.atual = self.atual + 0.06  
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))

allPlayerSprite = pygame.sprite.Group()
playerSprite = PlayerSprite()
allPlayerSprite.add(playerSprite)
                    
#código que pega o evento do teclado tem que ficar aqui