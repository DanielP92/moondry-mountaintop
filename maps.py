import os
import pygame
import pytmx
import global_vars as g
import base_map as m
import drops as d

current_dir = os.path.dirname("game.py")

class FarmMap(m.Map):
    def __init__(self, screen):
        super().__init__()
        self.filename = 'assets/maps/map.tmx'
        self.game_map = pytmx.load_pygame(os.path.join(current_dir, self.filename))
        self.screen = screen

        self.tw = self.game_map.tilewidth
        self.th = self.game_map.tileheight
        self.tw_count = self.game_map.width
        self.th_count = self.game_map.height
        self.width = self.tw * self.tw_count
        self.height = self.th * self.th_count

        self.tiles = []
        self.tree_top_tiles = []
        self.objects = {'terrain': [], 'bushes': [], 'rocks': [], 'other': []}
        self.shaders = []
        self.tile_group = pygame.sprite.Group()
        self.object_group = pygame.sprite.Group()
        self.tree_tops = pygame.sprite.Group()

        self.crafting = {'wood': [[500, 300]],
                         'stone': [[550, 325]],
                         'ore': [[600, 350]]}
        self.crafting_group = pygame.sprite.Group()

        self.camera = m.Camera(self.width, self.height)
        self.set_layers()


    def set_layers(self):

        def set_trees_and_water(tile_info):
            if tile_info['Name'] == 'TreeAllow':
                tile_sprite = m.TreeTop(tile, self.screen, x * self.tw, y * self.tw, self.tw, self.th)
                self.tree_tops.add(tile_sprite)
                self.tree_top_tiles.append((tile, tile_sprite))
            elif tile_info['Name'] == 'TreeBlock':
                tile_sprite = m.Tree(tile, x * self.tw, y * self.tw, self.tw, self.th)
                self.objects['terrain'].append((tile, tile_sprite))
                self.object_group.add(tile_sprite)
            elif tile_info['Name'] == 'Water':
                tile_sprite = m.Water(tile, x * self.tw, y * self.tw, self.tw, self.th)
                self.objects['terrain'].append((tile, tile_sprite))
                self.object_group.add(tile_sprite)
                
        for layer in self.game_map.visible_layers:
            if layer.name in ['Trees', 'Trees2', 'Trees3', 'Water']:
                for x, y, gid, in layer:
                    tile = self.game_map.get_tile_image_by_gid(gid)
                    if tile:
                        tile_info = self.game_map.get_tile_properties_by_gid(gid)
                        set_trees_and_water(tile_info)

            elif layer.name == 'Terrain':
                for x, y, gid in layer:
                    tile = self.game_map.get_tile_image_by_gid(gid)
                    tile_sprite = m.ObjTile(tile, x, y)
                    if tile:
                        self.objects['terrain'].append((tile, tile_sprite))

            elif layer.name in ["Base", "Shaders"]:
                for x, y, gid, in layer:
                    tile = self.game_map.get_tile_image_by_gid(gid)
                    tile_sprite = m.ObjTile(tile, x * self.tw, y * self.th)
                    if tile:
                       self.tiles.append((tile, tile_sprite))
                       self.tile_group.add(tile_sprite)

            elif layer.name == "ObjectShadows":
                for obj in layer:
                    if obj.image:
                        obj_sprite = m.ObjTile(obj, obj.x, obj.y)
                        self.shaders.append((obj.image, obj_sprite))

            elif layer.name == "Collisions":
                for obj in layer:
                    if obj.image:
                        if obj.name == "Bush":
                            obj_sprite = m.Bush(obj, obj.x, obj.y)
                            self.objects['bushes'].append((obj, obj_sprite))
                            g.all_sprites.add(obj_sprite)
                            g.bush_sprites.add(obj_sprite)
                            obj_sprite.level = self
                        elif obj.name == "Rock":
                            obj_sprite = m.Rock(obj, obj.x, obj.y)
                            self.objects['rocks'].append((obj, obj_sprite))
                            g.all_sprites.add(obj_sprite)
                            g.stone_sprites.add(obj_sprite)
                            obj_sprite.level = self
                        elif obj.name == None:
                            obj_sprite = m.Misc(obj, obj.x, obj.y)
                            self.objects['other'].append((obj, obj_sprite))

                        self.object_group.add(obj_sprite)

        for item in self.crafting['wood']:
            width = height = 20
            item_sprite = d.Wood(item[0], item[1], width, height)
            self.crafting_group.add(item_sprite)

        for item in self.crafting['stone']:
            width = height = 20
            item_sprite = d.Stone(item[0], item[1], width, height)
            self.crafting_group.add(item_sprite)
        
        for item in self.crafting['ore']:
            width = height = 20
            item_sprite = d.Ore(item[0], item[1], width, height)
            self.crafting_group.add(item_sprite)


    def draw(self, player):
        for tile in self.tiles + self.shaders + self.objects['terrain']:
            self.screen.blit(tile[0], self.camera.apply(tile[1]))

        for obj in self.objects['bushes'] + self.objects['rocks'] + self.objects['other']:
            obj_surface = pygame.Surface((int(obj[1].width), int(obj[1].height)))
            obj_image = obj_surface.blit(obj_surface, (0, 0))
            self.screen.blit(obj[1].current_img, self.camera.apply(obj[1]))

        for item in self.crafting_group:
            self.screen.blit(item.image, self.camera.apply(item))
        
        for sprite in g.active_sprite_list:
            self.screen.blit(sprite.current_sprite, self.camera.apply(sprite))

        for tile in self.tree_top_tiles:
            self.screen.blit(tile[0], self.camera.apply(tile[1]))

        self.camera.update(player)
        self.crafting_group.update()
        self.object_group.update()
