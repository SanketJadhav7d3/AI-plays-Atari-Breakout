
import pygame
import numpy as np
import random


class Tile(pygame.sprite.Sprite):
    def __init__(self, color, x=0, y=0):
        super(Tile, self).__init__()
        self.surf = pygame.Surface((50, 10)).convert_alpha()
        self.rect = self.surf.get_rect(x=x, y=y)
        self.surf.fill(color)

    @staticmethod
    def create_tile(x, y, color):
        return Tile(color, x, y)


class Tiles:

    def __init__(self, window):
        self.window = window
        self.win_width, self.win_height = self.window.get_size()
        self.tiles = pygame.sprite.Group()
        self.rows = 8
        self.columns = 10
        self.colors = [tuple(np.random.choice(range(256), size=3)) for _ in range(self.rows)]
        for i in range(self.columns):
            for j in range(self.rows):
                pos_x = i * (50)
                pos_y = j * (10)
                self.tiles.add(Tile.create_tile(pos_x, pos_y, self.colors[j]))
