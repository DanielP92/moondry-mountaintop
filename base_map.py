import os
import pygame
import pytmx
from global_vars import *
import player as p

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
    def __init__(self, obj, x, y):
        super().__init__()
        self.obj = obj
        self.x, self.y = x, y
        self.width = self.height = 32
        self.image = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


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


class Bush(ObjTile):
    def __init__(self, obj, x, y):
        super().__init__(obj, x, y)
        self.width = self.height = 28
        self.image = self.obj
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)