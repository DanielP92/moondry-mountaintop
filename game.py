import os
import pygame
import pytmx
from player import Player
from animation import Animate
import global_vars as g
import maps as m

current_dir = os.path.dirname("game.py")

def main():
    pygame.init()
    screen = pygame.display.set_mode([g.SCREEN_W, g.SCREEN_H])
    game_map = m.FarmMap(screen)
    clock = pygame.time.Clock()
    done = False
    player = Player(game_map, screen)
    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(player)
    print(" ".join("Welcome to Moondry Mountaintop"))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                if event.key == pygame.K_UP:
                    player.move_up()
                if event.key == pygame.K_DOWN:
                    player.move_down()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.change_y < 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.change_y > 0:
                    player.stop()

        active_sprite_list.update()
        game_map.draw(player)
        clock.tick(30)
        pygame.display.flip()

    quit()

if __name__ == "__main__":
    main()