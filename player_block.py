
import pygame
from pygame.locals import *
import neat


class AllPaddles:

    def __init__(self, window, genomes, config):
        self.window = window
        self.genomes = genomes
        self.config = config
        self.genome_count = len(self.genomes)
        # contains all the sprites for all the players
        # each sprite contains the genome_id
        self.paddles_sprites = pygame.sprite.Group()
        for genome_id, genome in self.genomes:
            genome.fitness = 0
            self.paddles_sprites.add(Player.create_paddle(self.window, genome, genome_id, config))

    def ballcollide(self, ball, score):
        if pygame.sprite.spritecollide(ball, self.paddles_sprites, dokill=False):
            # remove all the sprites execpt the ones from sprite_list
            sprite_list = pygame.sprite.spritecollide(ball, self.paddles_sprites, dokill=False)
            for sprite in self.paddles_sprites:
                if sprite not in sprite_list:
                    sprite.kill()
                    continue
            ball.change_direction()



class Player(pygame.sprite.Sprite):

    def __init__(self, window, genome, genome_id, config):
        super(Player, self).__init__()
        self.surf = pygame.Surface((90, 10))
        self.genome_id = genome_id
        self.window = window
        self.genome = genome
        self.surf.fill((255, 255, 255))
        self.win_width, self.win_height = self.window.get_size()
        self.rect = self.surf.get_rect(center=(self.win_width/2, self.win_height - 100))
        self.config = config

        # Network object
        self.net = neat.nn.FeedForwardNetwork.create(self.genome, self.config)

    def calculate_output(self, ball_rect):
        ball_center_x = ball_rect.center[0]
        ball_center_y = ball_rect.center[1]
        # input to the network 
        # player_paddle center x
        # ball center x and center y
        return self.net.activate((self.get_center_x(), ball_center_x, ball_center_y))

    def move(self, decision):

        if decision == 2:
            # move right
            self.move_right()
        elif decision == 1:
            # move left
            self.move_left()
        else:
            # stay still
            pass

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

    def get_center_x(self):
        return self.rect.center[0]

    def update_genome(self, score):
        self.genome.fitness += score

    @staticmethod
    def create_paddle(window, genome, genome_id, config):
        return Player(window, genome, genome_id, config)
