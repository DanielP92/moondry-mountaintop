import pygame

class BaseWield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class PickAxe(BaseWield):
    def __init__(self, target):
        super().__init__()
        self.target = target
