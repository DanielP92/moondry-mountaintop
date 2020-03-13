import os
import pygame
from base_character import Character
from animation import Animate
from images import PlayerImages


class Player(Character):
    images = PlayerImages("m_blonde_sprites.png")
    spritesheet = images.sprite_list

    def __init__(self, game_map, screen):
        super().__init__()
        self.game_map = game_map
        self.screen = screen
        self.width = self.height = 16
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = 410
        self.rect.y = 300
        self.animation = Animate(screen, self)
        self.animation_counter = self.animation_step = 0
        self.counter = 0
        self.group = pygame.sprite.Group()
        self.current_sprite = self.image
        self.current_sprites = [self.images.sprite_dict['down'][1] for x in range(2)]

    def update(self):
        self.animation.update()
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.collisions()

    def collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.game_map.object_group, False)
        for obj in collisions:
            if self.change_x > 0:
                self.rect.right = obj.rect.left
                obj.props['destroyed'] = True
                self.stop()
            elif self.change_x < 0:
                self.rect.left = obj.rect.right
                obj.props['destroyed'] = True
                self.stop()
            elif self.change_y > 0:
                self.rect.bottom = obj.rect.top
                obj.props['destroyed'] = True
                self.stop()
            elif self.change_y < 0 :
                self.rect.top = obj.rect.bottom
                obj.props['destroyed'] = True
                self.stop()

        wood = pygame.sprite.spritecollide(self, self.game_map.crafting_group, False)
        for obj in wood:
            col = pygame.sprite.collide_rect(self, obj)
            if col:
                obj.pick_up()

    def move_left(self):
        super().move_left()
        self.current_sprites = self.images.sprite_dict['left']

    def move_right(self):
        super().move_right()
        self.current_sprites = self.images.sprite_dict['right']

    def move_up(self):
        super().move_up()
        self.current_sprites = self.images.sprite_dict['up']

    def move_down(self):
        super().move_down()
        self.current_sprites = self.images.sprite_dict['down']

    def stop(self):
        super().stop()
        self.current_sprites = [self.current_sprites[1] for x in range(2)]

    def mine(self):
        pass

    def chop(self):
        pass

    def till(self):
        pass
