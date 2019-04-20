import pygame
import sys

# My modules
import utils

pygame.init()

# Screen settings
SIZE_WINDOW = width, height = 800, 800
RECTENGLES = []
PLAYER = x, y = 200, 40
SCREEN = None
STATUS = False

# Definitions colors
LIGHT_GREEN = (146, 255, 20)
DARK_GREEN = (58, 221, 19)
WHITE = (255, 255, 255)

SCREEN = pygame.display.set_mode(SIZE_WINDOW)
clock = pygame.time.Clock()

scene_utils = utils.reset_scene(pygame, SCREEN, DARK_GREEN, LIGHT_GREEN, WHITE, RECTENGLES)

pygame.display.flip()

while not STATUS:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STATUS = True

