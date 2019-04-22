from pygame import sprite, image


class Snake(sprite.Sprite):
    screen_size = [800, 800]
    screen = None
    rect = None
    movment_speed = 20
    x = 240
    y = 40
    size = 64
    color = (255, 18, 18)

    def __init__(self, screen):
        super() .__init__()
        self.image = image.load("head.png")
        self.screen = screen

    def moveup(self):
        if self.y <= 0:
            self.y = 0
        else:
            self.y -= self.movment_speed

    def movedown(self):
        if self.y >= self.screen_size[0] - self.size:
            self.y = self.screen_size[0] - self.size
        else:
            self.y += self.movment_speed

    def moveleft(self):
        if self.x <= 0:
            self.x = 0
        else:
            self.x -= self.movment_speed

    def moveright(self):
        if self.x >= self.screen_size[1] - self.size:
            self.x = self.screen_size[1] - self.size
        else:
            self.x += self.movment_speed

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
