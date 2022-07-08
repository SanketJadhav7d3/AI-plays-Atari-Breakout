
import pygame
from pygame.locals import *


class AllPaddles:

    def __init__(self, window, genomes):
        self.window = window
        self.genomes = genomes
        self.genome_count = len(self.genomes)
        self.paddles_sprites = pygame.sprite.Group()
        for genome_id, genome in self.genomes:
            self.all_paddles.add(Player.create_paddle(self.window, genome_id))


class Player(pygame.sprite.Sprite):

    def __init__(self, window, genome_id=0):
        super(Player, self).__init__()
        self.surf = pygame.Surface((90, 10))
        self.id = genome_id
        self.window = window
        self.surf.fill((255, 255, 255))
        self.win_width, self.win_height = self.window.get_size()
        self.rect = self.surf.get_rect(center=(self.win_width/2, self.win_height - 100))

    def move(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)

        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(10,  0)

        # don't let thw player get out of the window
        if self.rect.right >= self.win_width:
            self.rect.left = self.win_width - 90

        if self.rect.left <= 0:
            self.rect.left = 0


    def move_left(self):
        self.rect.move_ip(-12, 0)
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.move_ip(12, 0)

        if self.rect.right >= self.win_width:
            self.rect.left = self.win_width - 90

    @staticmethod
    def create_paddle(window, genome_id):
        return Player(window, genome_id)
