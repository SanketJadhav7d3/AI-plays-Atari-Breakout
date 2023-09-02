
import pygame
from ball import Ball
from pygame.locals import *
from tiles import Tiles
import neat
import os
from player_block import AllPaddles
import random
import matplotlib.pyplot as plt
import numpy as np
import visualize

pygame.init()


W = 500
H = 650


class Breakout:

    def __init__(self, W, H):
        self.W = W
        self.H = H
        self.window = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Atari Breakout")
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
        if self.all_players.ballcollide(self.ball):
            self.ball.change_direction()

        n = pygame.sprite.spritecollide(self.ball, self.tiles.tiles, dokill=True)
        if n:
            for _ in range(len(n)):
                self.score += 10
            print("Fitness Score:", self.score)
            print("Remaining targets:", len(self.tiles.tiles))
            self.ball.change_direction()

    def test_ai(self, genome):
        running = True
        clock = pygame.time.Clock()

        while running:
            # set fps to 60
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pressed_keys = pygame.mouse.get_pressed()

            self.draw()
            self.loop()
        pygame.quit()

    def train_ai(self, genomes, config):

        running = True

        clock = pygame.time.Clock()

        rand_x = np.random.randint(10, high=450)

        # random ball x position
        print("Ball initial coordiantes: ", rand_x, 200)
        self.ball.rect = self.ball.surf.get_rect(center=(rand_x, 200))

        # random ball direction
        self.ball.vel_x = random.choice([5, -5])

        # net = neat.nn.FeedForwardNetwork.create(genome, config)
        self.all_players = AllPaddles(self.window, genomes, config)

        self.all_sprites.add(self.all_players.paddles_sprites)

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

            if self.score >= 800 or ball_rect.bottom >= self.H - 40:
                for genome in self.all_players.paddles_sprites:
                    genome.update_genome(self.score)
                break

            self.loop()
            self.draw()


def eval_genomes(genomes, config):
    game = Breakout(W, H)
    game.train_ai(genomes, config)


def run(config_path):
    # load configuration
    # config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                           # neat.DefaultSpeciesSet, neat.DefaultStagnation,
                           # config_path)
    # population
    # p = neat.Population(config)

    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-32')

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 40)

    mean_fitness_score = stats.get_fitness_mean()
    
    # plt.plot(np.arange(0, len(mean_fitness_score)), mean_fitness_score)

    # visualize.draw_net(config, winner, True, show_disabled=False)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    # plt.xlabel("Generations")
    # plt.ylabel("Mean Fitness score")
    # plt.show()

    print("we have got the winner: {}".format(winner))

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
