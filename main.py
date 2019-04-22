import pygame

# My modules
import render
import player

pygame.init()

# Screen settings
SIZE_WINDOW = width, height = 800, 800
GAME_TABLE = None
SCREEN = None
STATUS = False

# Definitions colors
LIGHT_GREEN = (146, 255, 20)
DARK_GREEN = (58, 221, 19)
WHITE = (255, 255, 255)

SCREEN = pygame.display.set_mode(SIZE_WINDOW)
pygame.display.set_caption("PySnake")
clock = pygame.time.Clock()
GAME_TABLE = render.Rendering(SCREEN, DARK_GREEN, LIGHT_GREEN, WHITE)
snake = player.Snake(SCREEN)
snakegroup = pygame.sprite.Group()
snakegroup.add(snake)
snakegroup.update()
pygame.display.flip()

while not STATUS:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STATUS = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snake.moveleft()
    if keys[pygame.K_RIGHT]:
        snake.moveright()
    if keys[pygame.K_DOWN]:
        snake.movedown()
    if keys[pygame.K_UP]:
        snake.moveup()
    render.Rendering(SCREEN, DARK_GREEN, LIGHT_GREEN, WHITE)
    snake.draw()
    pygame.display.update()

pygame.quit()
