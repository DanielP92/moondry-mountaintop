import pygame
from items import Item
from images import TransparentIcons

class Drop(Item):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height

    def update(self):
        pass

class Ore(Drop):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

class Wood(Drop):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.surface = pygame.Surface((int(self.rect.width), int(self.rect.height)))
        self.image = TransparentIcons("transparent_icons.png").sprite_dict['wood']
        self.change_y = 1
        self.counter = 0

    def update(self):
        self.rect.y += self.change_y
        self.counter += 0.5
        if self.counter >= 5:
            self.change_y = -self.change_y
            self.counter = 0

    def pick_up(self):
        self.kill()
