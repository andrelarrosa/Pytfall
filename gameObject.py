from screen import Screen

class GameObject:
    def __init__(self, x: int, y: int, width: int, height: int, vel_x: float, vel_y: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel_x = vel_x
        self.vel_y = vel_y

    def atualizarPosicaoObjeto(self):
        novaPosicaoX = self.x + self.vel_x * pygame.time.Clock().tick(60)
        self.x = novaPosicaoX

        novaPosicaoY = self.y + self.vel_y * pygame.time.Clock().tick(60)
        self.y = novaPosicaoY
    def desenharObjeto(screen: Screen):
        RED = (255, 0, 0)
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        pygame.display.update()