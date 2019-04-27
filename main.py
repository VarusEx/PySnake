import pygame

# My modules
import render
import player
from food import Food

pygame.init()

# Screen settings
SIZE_WINDOW = width, height = 800, 800
GAME_TABLE = None
FOOD = max, current = 5, 0
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
pos = snake.get_pos()
tail = player.Tail(pos[0], pos[1], SCREEN)
snake.body_elements.append(tail)
tail.master = snake
foodgroup = pygame.sprite.Group()
pygame.display.flip()

while not STATUS:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STATUS = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snake.moveleft()
    elif keys[pygame.K_RIGHT]:
        snake.moveright()
    elif keys[pygame.K_DOWN]:
        snake.movedown()
    elif keys[pygame.K_UP]:
        snake.moveup()
    GAME_TABLE = render.Rendering(SCREEN, DARK_GREEN, LIGHT_GREEN, WHITE)

    if current < max:
        current += 1
        food = Food(SCREEN)
        foodgroup.add(food)
        food.draw(SCREEN, snake.get_pos())
        foodgroup.update()
    for c in foodgroup:
        c.redraw(SCREEN)
        if pygame.sprite.collide_rect(snake, c):
            current -= 1
            snake.set_points(c.get_points())
            c.kill()
    snake.draw()
    tail.draw()
    render.Rendering.show_points(GAME_TABLE, points=snake.get_points())
    pygame.display.update()

pygame.quit()
