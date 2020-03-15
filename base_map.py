import os
import pygame
import pytmx
from global_vars import *
import player as p
from images import MapImages

current_dir = os.path.dirname("game.py")

class Map:

    def __init__(self):
        self.filename = ''
        self.game_map = pytmx.load_pygame(os.path.join(current_dir, self.filename))
        self.width = 0
        self.height = 0
        self.camera = Camera(self.width, self.height)
        pygame.init()

    def draw(self, screen):
        pass


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        if isinstance(entity, p.Player):
            return entity.rect.move((self.camera.topleft[0] - 5, self.camera.topleft[1] - 16))
        else:
            return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(SCREEN_W / 2)
        y = -target.rect.y + int(SCREEN_H / 2)
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - SCREEN_W), x)
        y = max(-(self.height - SCREEN_H), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)


class ObjTile(pygame.sprite.Sprite):
    images = MapImages('BaseChip_pipo.png').sprite_dict
    def __init__(self, obj, x, y):
        super().__init__()
        self.obj = obj
        self.x, self.y = x, y
        self.width = self.height = 32
        self.image = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.current_img = self.image


class Tree(ObjTile):
    def __init__(self, obj, x, y, width, height):
        super().__init__(obj, x ,y)
        self.width, self.height = width, height
        self.image = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class TreeTop(ObjTile):
    def __init__(self, obj, screen, x, y, width, height):
        super().__init__(obj, x ,y)
        self.width, self.height = width, height
        self.screen = screen
        self.image = pygame.Surface((self.width, self.height))


class Destroyable(ObjTile):
    def __init__(self, obj, x, y):
        super().__init__(obj, x, y)
        self.width = self.height = 28
        self.image = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.counter = 0
        self.props = self.obj.properties
        self.props['destroyed'] = False
        self.orig_img = self.obj.image
        self.destroyed_img = None
        self.current_img = self.orig_img

    def update(self):
        if self.props['destroyed']:
            self.counter += 1
            self.current_img = self.destroyed_img

        if self.counter >= 45:
            self.props['destroyed'] = False
            self.counter = 0
            self.current_img = self.orig_img


class Bush(Destroyable):
    def __init__(self, obj, x, y):
        super().__init__(obj, x, y)
        self.destroyed_img = self.images['stump']


class Rock(Destroyable):
    def __init__(self, obj, x, y):
        super().__init__(obj, x, y)
        self.destroyed_img = self.images['rubble']

class Misc(Destroyable):
    def __init__(self, obj, x, y):
        super().__init__(obj, x, y)
        self.destroyed_img = self.current_img
