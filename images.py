import os
import pygame

current_dir = os.path.dirname('game.py')
resource_dir = os.path.join(current_dir, 'libraries')
img_dir = os.path.join(resource_dir, 'imgs')
player_dir = os.path.join(img_dir, 'player')

class Images:
    def __init__(self, file):
        self.file = file
        self.path = os.path.join(player_dir, self.file)
        self.sprites = pygame.image.load(self.path)
        self.width, self.height = self.sprites.get_width(), self.sprites.get_height()
        self.img_size = 32

    def set_sprites(self):
        self.sprite_list = []

        for i in range(0, self.height, self.img_size):
            for j in range(0, self.width, self.img_size):
                self.sprite_list.append(self.sprites.subsurface(j, i, self.img_size, self.img_size))


class PlayerImages(Images):
    def __init__(self, file):
        super().__init__(file)
        self.sprite_list = []

        for i in range(0, self.height, self.img_size):
            for j in range(0, self.width, self.img_size):
                self.sprite_list.append(self.sprites.subsurface(j, i, self.img_size, self.img_size))

        self.sprite_dict = {'down': [self.sprite_list[0], self.sprite_list[1], self.sprite_list[2], self.sprite_list[1]],
                            'left': [self.sprite_list[3], self.sprite_list[4], self.sprite_list[5], self.sprite_list[4]],
                            'right': [self.sprite_list[6], self.sprite_list[7], self.sprite_list[8], self.sprite_list[7]],
                            'up': [self.sprite_list[9], self.sprite_list[10], self.sprite_list[11], self.sprite_list[10]],
                            }

class TransparentIcons(Images):
    def __init__(self, file):
        super().__init__()
        