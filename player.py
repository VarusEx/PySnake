from pygame import sprite, image, transform, display


class Snake(sprite.Sprite):
    screen_size = [800, 800]
    screen = None
    __rect = None
    __angle = 0
    __points = 0
    body_elements = []
    movment_speed = 20
    _x = 240
    _y = 200
    __width, __height = 64, 64

    def __init__(self, screen):
        super() .__init__()
        self.image = image.load("resources\\top.png")
        self.rect = self.image.get_rect()
        self.set_angle(180)
        self.screen = screen

    def moveup(self):
        self.set_angle(0)
        if self._y <= 0:
            self._y = 0
            self.rect.top = 0
        else:
            self._y -= self.movment_speed
            self.rect.top -= self.movment_speed
        self.body_elements[0].moveup()

    def movedown(self):
        self.set_angle(180)
        if self._y >= self.screen_size[0] - self.__height:
            self._y = self.screen_size[0] - self.__height
            self.rect.bottom = self.screen_size[1] - self.__height
        else:
            self._y += self.movment_speed
            self.rect.bottom += self.movment_speed
        self.body_elements[0].movedown()

    def moveleft(self):
        self.set_angle(270)
        if self._x <= 0:
            self.rect.left = 0
            self._x = 0
        else:
            self._x -= self.movment_speed
            self.rect.left -= self.movment_speed
        self.body_elements[0].moveleft()

    def moveright(self):
        self.set_angle(90)
        if self._x >= self.screen_size[1] - self.__width:
            self._x = self.screen_size[1] - self.__width
            self.rect.right = self.screen_size[1] - self.__width
        else:
            self._x += self.movment_speed
            self.rect.right += self.movment_speed
        self.body_elements[0].moveright()

    def draw(self):
        self.rect.top = self._y
        self.rect.right = self._x
        self.screen.blit(self.image, (self._x, self._y))

    def set_speed(self, speed):
        self.movment_speed = speed

    def set_size(self, width, height):
        self.image = transform.scale(self.image, (width, height))
        for obj in self.body_elements:
            obj.image = transform.scale(obj.image, (width, height))
            obj.width, obj.height = width, height
        self.__width, self.__height = width, height

    def set_pos(self, _x, _y):
        self._x, self._y = _x, _y
        self.draw()

    def set_image(self, img):
        self.image = image.load(img)

    def set_angle(self, angle):
        if angle == self.__angle:
            return
        self.image = transform.rotate(self.image, self.__angle - angle)
        self.__angle = angle

    def set_points(self, a):
        self.__points += a

    def get_pos(self):
        return self._x, self._y

    def get_size(self):
        return self.__width, self.__height

    def get_player_image(self):
        return self.image

    def get_speed(self):
        return self.movment_speed

    def get_rect(self):
        return self.__rect

    def get_angle(self):
        return self.__angle

    def get_points(self):
        return self.__points


class Tail(Snake):
    rect = None
    master = None
    angle = 0
    x, y = 240, 160
    width, height = 60, 60

    def __init__(self, x, y, screen):
        super().__init__(screen=screen)
        self.image = image.load("resources\\tail.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x, self.y = x, y - self.height

    def draw(self):
        self.rect.top = self.y
        self.rect.right = self.x
        self.screen.blit(self.image, (self.x, self.y))

    def moveup(self):
        self.set_angle(0)
        self.y = self.master.get_pos()[1] + self.master.get_size()[1] - 4
        self.x = self.master.get_pos()[0]

    def movedown(self):
        self.set_angle(180)
        self.y = self.master.get_pos()[1] - self.master.get_size()[1] + 4
        self.x = self.master.get_pos()[0]

    def moveleft(self):
        self.set_angle(270)
        self.y = self.master.get_pos()[1]
        self.x = self.master.get_pos()[0] + self.master.get_size()[0] - 4

    def moveright(self):
        self.set_angle(90)
        self.y = self.master.get_pos()[1]
        self.x = self.master.get_pos()[0] - self.master.get_size()[0] + 4

    def set_angle(self, angle):
        if angle == self.angle:
            return
        self.image = transform.rotate(self.image, self.angle - angle)
        self.angle = angle
