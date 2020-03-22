import pygame
import pytweening as tween
from items import Item
import global_vars as g


class BaseWield(pygame.sprite.Sprite):
    images = Item.item_sprites

    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.tween = tween.easeInOutElastic
        self.tween_range = 75
        self.speed = 2
        self.step = 0
        self.direction = 0.2
        self.col_sprite = pygame.sprite.Sprite()
        self.active = True
        g.all_sprites.add(self)

    def update(self):
        if self.active:
            self.use()

    def use(self):
        g.active_sprite_list.add(self)
        offset = self.tween_range * self.tween(self.step / self.tween_range)
        self.current_sprite = pygame.transform.rotate(self.image_clean, (45 - offset))
        self.rect.centerx = self.pos[0] + offset * self.direction + 16
        self.rect.centery = self.pos[1] + offset * self.direction - 16

        self.col_sprite.surface = self.current_sprite.subsurface(20, 25, 5, 5)
        self.col_sprite.rect = self.col_sprite.surface.get_rect()
        self.col_sprite.rect.centerx = self.pos[0] + offset * self.direction + 16
        self.col_sprite.rect.centery = self.pos[1] + offset * self.direction - 16
        self.col_sprite.active = False

        self.step += self.speed

        if self.step > 40:
            self.col_sprite.active = True

        if self.step >= self.tween_range:
            self.step = 0
            self.current_sprite = pygame.transform.rotate(self.image_clean, 45)
            self.rect.centerx = self.pos[0]
            self.rect.centery = self.pos[1]
            g.active_sprite_list.remove(self)
            g.all_sprites.remove(self)
            self.active = False
            self.col_sprite.active = False
        self.rect = self.current_sprite.get_rect(center = self.rect.center)


class PickAxe(BaseWield):
    def __init__(self, pos):
        super().__init__(pos)
        self.image_clean = self.images.sprite_dict['pickaxe']
        self.current_sprite = pygame.transform.rotate(self.image_clean, 45)
        self.rect = self.current_sprite.get_rect()
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]

    def use(self):
        super().use()
        for stone in g.stone_sprites:
            collision = pygame.sprite.collide_rect(self.col_sprite, stone)
            if collision and self.col_sprite.active:
                stone.props['destroyed'] = True


class Axe(BaseWield):
    def __init__(self, pos):
        super().__init__(pos)
        self.image_clean = self.images.sprite_dict['axe']
        self.current_sprite = pygame.transform.rotate(self.image_clean, 45)
        self.rect = self.current_sprite.get_rect()
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]

    def use(self):
        super().use()
        for bush in g.bush_sprites:
            collision = pygame.sprite.collide_rect(self.col_sprite, bush)
            if collision and self.col_sprite.active:
                bush.props['destroyed'] = True
