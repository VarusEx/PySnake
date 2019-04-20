import pygame

# My modules
import render

pygame.init()

# Screen settings
SIZE_WINDOW = width, height = 800, 800
GAME_TABLE = None
SCREEN = None
STATUS = False
snake = None

# Definitions colors
LIGHT_GREEN = (146, 255, 20)
DARK_GREEN = (58, 221, 19)
WHITE = (255, 255, 255)


class PlayerClass:
    PLAYER_Pos = x, y = 200, 40
    player_x = 200
    player_y = 40
    SPEED = 40

    def __init__(self, engine, screen):
        self.spawn(engine, screen)

    def spawn(self, engine, screen):
        snake = engine.draw.circle(screen, (255, 18, 18), [self.player_x, self.player_y], 20)
        return snake

    def moveup(self):
        if self.player_y <= 0:
            self.player_y = 0
        else:
            self.player_y -= self.SPEED

    def movedown(self):
        if self.player_y >= SIZE_WINDOW[1] - self.player_y:
            self.player_y = SIZE_WINDOW[1] - self.player_y
        else:
            self.player_y += self.SPEED

    def moveleft(self):
        if self.player_y <= 0:
            self.player_y = 0
        else:
            self.player_y -= self.SPEED

    def moveright(self):
        if self.player_x >= SIZE_WINDOW[0] - self.player_x:
            self.player_x = SIZE_WINDOW[0] - self.player_x
        else:
            self.player_x += self.SPEED


SCREEN = pygame.display.set_mode(SIZE_WINDOW)
clock = pygame.time.Clock()
GAME_TABLE = render.Rendering(pygame, SCREEN, DARK_GREEN, LIGHT_GREEN, WHITE)
snake = PlayerClass(pygame, SCREEN)
pygame.display.flip()

while not STATUS:
    clock.tick(60)
    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
        snake.moveup()
    if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
        snake.movedown()
    if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        snake.moveleft()
    if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        snake.moveright()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STATUS = True
    pygame.display.update()
