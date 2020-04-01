import random
import pygame
import pytweening as tween
from items import Item


class Drop(Item):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height
        self.surface = pygame.Surface((int(self.rect.width), int(self.rect.height)))
        self.image = self.surface
        self.change_y = 1
        self.counter = 0
        self.active = False
        self.tween = random.choice([tween.easeOutQuint, tween.easeOutQuart, tween.easeInExpo, tween.easeOutExpo])
        self.tween_range = 10
        self.speed = 0.5
        self.directionx = random.choice([-0.2, 0.2])
        self.directiony = random.choice([-0.2, 0.2])
        self.step = 0

    def update(self):
        self.rect.y += self.change_y
        self.counter += 0.5
        if self.counter >= 5:
            self.change_y = -self.change_y
            self.counter = 0
        if self.active:
            self.spread()

    def pick_up(self):
        self.kill()
        
    def spread(self):
        offset = self.tween_range * self.tween(self.step / self.tween_range)
        self.rect.x += offset * self.directionx
        self.rect.y += offset * self.directiony
        self.step += self.speed 
        if self.step >= self.tween_range:
            self.active = False


class Ore(Drop):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = self.item_sprites.sprite_dict['ore']

    def __str__(self):
        return 'Ore'

    def pick_up(self):
        super().pick_up()


class Wood(Drop):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = self.item_sprites.sprite_dict['wood']

    def __str__(self):
        return 'Wood'

    def pick_up(self):
        super().pick_up()


class Stone(Drop):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = self.item_sprites.sprite_dict['stone']

    def __str__(self):
        return 'Stone'
        
    def pick_up(self):
        super().pick_up()
