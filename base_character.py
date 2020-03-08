from global_vars import *
import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = self.height = 0
        self.change_x = self.change_y = 0

    def move_horiz(self):
        self.change_y = 0

    def move_verti(self):
        self.change_x = 0

    def move_left(self):
        self.move_horiz()
        self.change_x = -3

    def move_right(self):
        self.move_horiz()
        self.change_x = 3

    def move_up(self):
        self.move_verti()
        self.change_y = -3

    def move_down(self):
        self.move_verti()
        self.change_y = 3

    def stop(self):
        self.change_x = self.change_y = 0
