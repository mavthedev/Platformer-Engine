import pygame
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: int):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('gray')
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, x_shift):
        self.rect.x += x_shift
class Coin(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: int):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, x_shift):
        self.rect.x += x_shift
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: int):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, x_shift):
        self.rect.x += x_shift