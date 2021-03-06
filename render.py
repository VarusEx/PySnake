import pygame


class Rendering(pygame.Surface):
    RECTENGLES = []
    SCREEN = None

    def __init__(self, screen, color_1, color_2, color_bg):
        super().__init__((800, 800))
        self.SCREEN = screen
        self.set_background(screen)
        self.reset_scene(color_1, color_2, self.RECTENGLES)

    def reset_scene(self, color_1, color_2, container):
        i, x, y = 1, 0, 0
        for i in range(0, 6):
            container += self.draw_rectengle(0, y, color_1, loops=6)
            container += self.draw_rectengle(80, y, color_2, loops=6, case=2)
            y += 160
            if y == 800:
                y = 0
        for i in range(0, 6):
            container += self.draw_rectengle(80, y + 80, color_1, loops=6, case=2)
            container += self.draw_rectengle(0, y + 80, color_2, loops=6)
            y += 160
            if y == 800:
                y = 0

    def draw_rectengle(self, pos_x, pos_y, color, loops=5, case=1):
        rectengles = []
        i, x, y = 1, pos_x, pos_y
        while i in range(0, loops + 1):
            rect = pygame.draw.rect(self.SCREEN, color, [x, y, 80, 80])
            i += 1
            if case == 1:
                x += 160
                y += 0
            else:
                x += 160
            rectengles += [rect]
        return rectengles

    def show_points(self, points):
        font = pygame.font.Font(None, 80)
        text = str(points)
        size = font.size(text)
        font.set_underline(1)
        ren = font.render(text, 0, (13, 180, 255))
        self.SCREEN.blit(ren, (10, 40 + size[1]))
        font.set_underline(0)

    @staticmethod
    def set_background(screen, color_bg=(255, 255, 255)):
        return screen.fill(color_bg)

    @staticmethod
    def redraw_background(screen):
        screen.blit(source=screen.copy(), dest=(0, 0))


