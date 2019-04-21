import pygame


class Rendering(pygame.Surface):
    RECTENGLES = []
    SCREEN = None

    def __init__(self, screen, color_1, color_2, color_bg):
        super().__init__((800, 800))
        self.SCREEN = screen
        self.reset_scene(color_1, color_2, color_bg, self.RECTENGLES)

    def reset_scene(self, color_1, color_2, color_bg, container):
        i, x, y = 1, 0, 0
        bg = self.set_background(color_bg)
        for i in range(0, 6):
            container += self.draw_rectengle(0, y, color_1, loops=5)
            container += self.draw_rectengle(80, y, color_2, loops=5, case=2)
            y += 160
            if y == 800:
                y = 0
        for i in range(0, 6):
            container += self.draw_rectengle(80, y + 80, color_1, loops=5, case=2)
            container += self.draw_rectengle(0, y + 80, color_2, loops=5)
            y += 160
            if y == 800:
                y = 0
        return bg

    def set_background(self, color_bg=(255, 255, 255)):
        return self.SCREEN.fill(color_bg)
    @staticmethod
    def redraw_background(screen):
        s = screen.copy()
        screen.blit(source=s, dest=(0, 0))

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
