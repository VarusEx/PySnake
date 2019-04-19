def spawn_snake():
    pass


def move():
    pass


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
        rectengles += [rect, x, y]
        print(rect, x, y)
    return rectengles


def reset_scene(engine, screen, color_1, color_2, container):
    i, x, y = 1, 0, 0
    bg = set_background(screen, color_2)
    for i in range(0, 6):
        container += draw_rectengle(engine, 0, y, screen, color_1, loops=5)
        y += 160
        if y == 800:
            y = 0
    for i in range(0, 6):
        container += draw_rectengle(engine, 80, y + 80, screen, color_1, loops=5, case=2)
        y += 160
        if y == 800:
            y = 0

    return container, bg
