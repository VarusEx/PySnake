import pygame
import random


class Food(pygame.sprite.Sprite):
    screen = None
    rect = None
    x = 0
    y = 0
    points = 0
    size = width, height = 64, 64

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("resources\\apple.png")
        self.rect = self.image.get_rect()
        self.screen = screen

    @staticmethod
    def random_pos():
        return random.randint(0, 700)

    def redraw(self, screen):
        self.rect.top, self.rect.right = self.y, self.x
        return screen.blit(self.image, (self.x, self.y))

    def draw(self, screen, player_pos):
        self.x, self.y = self.random_pos(), self.random_pos()
        if self.x and self.y < 800 - self.size[0] and (self.x and self.y) != player_pos[0] + self.width:
            self.points = random.randint(0, 50)
            self.rect.top, self.rect.right = self.y, self.x
            return screen.blit(self.image, (self.x, self.y))
        self.draw(screen, player_pos)

    def set_points(self, a):
        self.points = a

    def set_pos(self, x, y):
        self.x, self.y = x, y
        self.redraw(self.screen)

    def set_size(self, width, height):
        pygame.transform.scale(self.image, (width, height))

    def set_image(self, img):
        self.image = pygame.image.load(img)

    def get_pos(self):
        return self.x, self.y

    def get_size(self):
        return self.width, self.height

    def get_player_image(self):
        return self.image

    def get_points(self):
        return self.points

    def get_rect(self):
        return self.rect

