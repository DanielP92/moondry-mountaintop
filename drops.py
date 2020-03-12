import pygame
from items import Item


class Drop(Item):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height
        self.surface = pygame.Surface((int(self.rect.width), int(self.rect.height)))
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


class Ore(Drop):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = self.item_sprites.sprite_dict['ore']

    def pick_up(self):
        super().pick_up()


class Wood(Drop):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = self.item_sprites.sprite_dict['wood']

    def pick_up(self):
        super().pick_up()


class Stone(Drop):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = self.item_sprites.sprite_dict['stone']
        
    def pick_up(self):
        super().pick_up()