import os
import pygame

current_dir = os.path.dirname('game.py')
resource_dir = os.path.join(current_dir, 'libraries')
img_dir = os.path.join(resource_dir, 'imgs')
player_dir = os.path.join(img_dir, 'player')
item_dir = os.path.join(img_dir, 'items')

class Images:
    def __init__(self, file):
        self.file = file
        self.img_size = 32
        self.sprite_list = []

    def set_surfaces(self):
        for i in range(0, self.height, self.img_size):
            for j in range(0, self.width, self.img_size):
                self.sprite_list.append(self.spritesheet.subsurface(j, i, self.img_size, self.img_size))


class PlayerImages(Images):
    def __init__(self, file):
        super().__init__(file)
        self.path = os.path.join(player_dir, self.file)
        self.spritesheet = pygame.image.load(self.path)
        self.width, self.height = self.spritesheet.get_width(), self.spritesheet.get_height()
        self.set_surfaces()

        self.sprite_dict = {'down': [self.sprite_list[0], self.sprite_list[1], self.sprite_list[2], self.sprite_list[1]],
                            'left': [self.sprite_list[3], self.sprite_list[4], self.sprite_list[5], self.sprite_list[4]],
                            'right': [self.sprite_list[6], self.sprite_list[7], self.sprite_list[8], self.sprite_list[7]],
                            'up': [self.sprite_list[9], self.sprite_list[10], self.sprite_list[11], self.sprite_list[10]],
                            }


class TransparentIcons(Images):
    def __init__(self, file):
        super().__init__(file)
        self.path = os.path.join(item_dir, self.file)
        self.spritesheet = pygame.image.load(self.path)
        self.width, self.height = self.spritesheet.get_width(), self.spritesheet.get_height()
        self.set_surfaces()

        self.sprite_dict = {'wood': self.sprite_list[272]}
