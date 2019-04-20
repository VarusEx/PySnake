def spawn_snake(engine, screen, x=0, y=0):
    snake = engine.draw.circle(screen, (255, 18, 18), [200 + x, 40 + y], 20)
    return snake


def move(engine, snake, pos_x, pos_y):
    snake.move([pos_x, pos_y])
    engine.display.update(snake)


def set_background(screen, color_bg=(255, 255, 255)):
    return screen.fill(color_bg)


def draw_rectengle(engine, pos_x, pos_y, screen, color, loops=5, case=1):
    rectengles = []
    i, x, y = 1, pos_x, pos_y
    while i in range(0, loops + 1):
        rect = engine.draw.rect(screen, color, [x, y, 80, 80])
        i += 1
        if case == 1:
            x += 160
            y += 0
        else:
            x += 160
        rectengles += [rect]
    return rectengles


def reset_scene(engine, screen, color_1, color_2, color_bg, container):
    i, x, y = 1, 0, 0
    bg = set_background(screen, color_bg)
    for i in range(0, 6):
        container += draw_rectengle(engine, 0, y, screen, color_1, loops=5)
        container += draw_rectengle(engine, 80, y, screen, color_2, loops=5, case=2)
        y += 160
        if y == 800:
            y = 0
    for i in range(0, 6):
        container += draw_rectengle(engine, 80, y + 80, screen, color_1, loops=5, case=2)
        container += draw_rectengle(engine, 0, y + 80, screen, color_2, loops=5)
        y += 160
        if y == 800:
            y = 0

    return bg, spawn_snake(engine, screen)
