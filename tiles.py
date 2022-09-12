
import pygame
import numpy as np


class Tile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super(Tile, self).__init__()
        self.surf = pygame.Surface((80, 10)).convert_alpha()
        self.rect = self.surf.get_rect(x=x, y=y)
        self.surf.fill((255, 255, 0))

    @staticmethod
    def create_tile(x, y):
        return Tile(x, y)


class Tiles:

    def __init__(self, window):
        self.window = window
        self.win_width, self.win_height = self.window.get_size()
        self.tiles = pygame.sprite.Group()
        self.count = 20
        self.tile_arr = np.ones(shape=(4, 5))
        for i in range(self.tile_arr.shape[0]):
            for j in range(self.tile_arr.shape[1]):
                pos_x = 10 + (j * (80 + 20))
                pos_y = 10 + (i * (10 + 20))
                self.tiles.add(Tile.create_tile(pos_x, pos_y))
