import pygame
import player as p
import base_map as b

class Animate:
    def __init__(self, screen, sprite):
        self.screen = screen
        self.sprite = sprite

    def update(self):
        self.draw()
        if isinstance(self.sprite, p.Player):
            self.sprite.current_sprite = self.sprite.current_sprites[self.sprite.animation_step]
        else:
            self.screen.blit(self.sprite, self.sprite.rect.x, self.sprite.rect.y)

    def draw(self):
        if isinstance(self.sprite, p.Player):
            self.sprite.group.draw(self.screen)
            self.sprite.animation_counter += 1
            if self.sprite.animation_counter >= 6:
                self.sprite.animation_step += 1
                self.sprite.animation_counter = 0
            if self.sprite.animation_step >= len(self.sprite.current_sprites):
                self.sprite.animation_step = 0
        else:
            pass
