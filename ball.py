
import pygame
import math


class Ball(pygame.sprite.Sprite):

    def __init__(self, window):
        super(Ball, self).__init__()
        self.window = window
        self.surf = pygame.Surface((20, 20)).convert_alpha()
        self.win_width, self.win_height = self.window.get_size()
        self.rect = self.surf.get_rect(center=(250, 200))
        self.vel_x, self.vel_y = 4, 4
        pygame.draw.circle(self.surf, (255, 255, 255), (10, 10), 10)

    def update(self):
        if self.rect.left < 0 or self.rect.right > self.win_width:
            self.vel_x = -self.vel_x
        elif self.rect.top < 0:
            self.vel_y = -self.vel_y
        self.rect.move_ip(self.vel_x, self.vel_y)

    def change_direction(self):
        self.vel_y = -self.vel_y

    def get_center(self):
        return self.rect.center
