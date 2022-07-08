#!/Users/sanketjadhav/opt/miniconda3/bin/python

import pygame
from ball import Ball
from player_block import Player
from pygame.locals import *
from tiles import Tiles
import neat
import os
from pygame.locals import *
from player_block import AllPaddles


pygame.init()

W = 500
H = 650


class Breakout:

    def __init__(self, W, H):
        self.W = W
        self.H = H
        self.window = pygame.display.set_mode((self.W, self.H))
        self.score = 0

        # ball sprite
        self.ball = Ball(self.window)

        # tiles sprites group
        self.tiles = Tiles(self.window)

        self.generation = 0

        # all sprites group
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.ball)
        self.all_sprites.add(self.tiles.tiles)

    def draw(self):
        '''
            Draws all the sprites components of the game
        '''
        for entity in self.all_sprites.sprites():
            self.window.blit(entity.surf, entity.rect)

        pygame.display.update()

    def loop(self):
        '''
            The main loop of the game
        '''
        # fill the window with black
        self.window.fill((0, 0, 0))

        self.ball.update()

        # check for the collision between the player sprites and the ball
        # if pygame.sprite.collide_rect(self.ball, self.player):
            # self.ball.change_direction()

        # contains the sprites which hit the ball 
        if self.all_players.ballcollide(self.ball, self.score):
            self.ball.change_direction()

        if pygame.sprite.spritecollide(self.ball, self.tiles.tiles, dokill=True):
            self.score += 10
            self.ball.change_direction()


    def test_ai(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            # set fps to 60
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pressed_keys = pygame.mouse.get_pressed()
            self.player.move(pressed_keys)

            self.draw()
            self.loop()
        pygame.quit()

    def train_ai(self, genomes, config):

        running = True
        clock = pygame.time.Clock()

        # net = neat.nn.FeedForwardNetwork.create(genome, config)
        self.all_players = AllPaddles(self.window, genomes, config)

        self.all_sprites.add(self.all_players.paddles_sprites)

        self.generation += 1

        pygame.display.set_caption("Generation: {}".format(self.generation))

        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.quit:
                    running = false

            ball_rect = self.ball.rect

            for genome in self.all_players.paddles_sprites:
                output = genome.calculate_output(ball_rect)

                decision = output.index(max(output))

                genome.move(decision)

            if self.score == 200 or ball_rect.bottom >= self.H - 90:
                # calculate the fitness
                # genome.fitness += self.score
                break

            self.loop()
            self.draw()


def eval_genomes(genomes, config):

    game = Breakout(W, H)
    game.train_ai(genomes, config)


def run(config_path):
    # load configuration
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    # population
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 40)

    print("we have got the winner: {}".format(winner))

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
