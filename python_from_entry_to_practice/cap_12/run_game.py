import os

import pygame
import sys


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')

    while True:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
