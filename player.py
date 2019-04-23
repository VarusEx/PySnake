from pygame import sprite, image, transform


class Snake(sprite.Sprite):
    screen_size = [800, 800]
    screen = None
    rect = None
    points = 0
    movment_speed = 20
    x = 240
    y = 40
    width, height = 64, 64

    def __init__(self, screen):
        super() .__init__()
        self.image = image.load("resources\\head.png")
        self.rect = self.image.get_rect()
        self.screen = screen

    def moveup(self):
        if self.y <= 0:
            self.y = 0
            self.rect.top = 0
        else:
            self.y -= self.movment_speed
            self.rect.top -= self.movment_speed

    def movedown(self):
        if self.y >= self.screen_size[0] - self.height:
            self.y = self.screen_size[0] - self.height
            self.rect.bottom = self.screen_size[1] - self.height
        else:
            self.y += self.movment_speed
            self.rect.bottom += self.movment_speed

    def moveleft(self):
        if self.x <= 0:
            self.rect.left = 0
            self.x = 0
        else:
            self.x -= self.movment_speed
            self.rect.left -= self.movment_speed

    def moveright(self):
        if self.x >= self.screen_size[1] - self.width:
            self.x = self.screen_size[1] - self.width
            self.rect.right = self.screen_size[1] - self.width
        else:
            self.x += self.movment_speed
            self.rect.right += self.movment_speed

    def draw(self):
        self.rect.top = self.y
        self.rect.right = self.x
        self.screen.blit(self.image, (self.x, self.y))

    def set_speed(self, speed):
        self.movment_speed = speed

    def set_size(self, width, height):
        transform.scale(self.image, (width, height))
        self.width, self.height = width, height

    def set_pos(self, x, y):
        self.x, self.y = x, y
        self.draw()

    def set_image(self, img):
        self.image = image.load(img)

    def set_points(self, a):
        self.points += a

    def get_pos(self):
        return self.x, self.y

    def get_size(self):
        return self.width, self.height

    def get_player_image(self):
        return self.image

    def get_speed(self):
        return self.movment_speed

    def get_rect(self):
        return self.rect
