import pygame

SQUARE = 40
BACKGROUND = (50, 240, 200)


class Snake:
    def __init__(self, screen, length):
        self.screen = screen
        self.length = length
        self.body = pygame.image.load("images/body.jpg").convert()
        self.direction = "right"
        self.x = [10] * length
        self.y = [10] * length

    def draw(self):
        for i in range(self.length):
            self.screen.blit(self.body, (self.x[i], self.y[i]))
        pygame.display.update()

    def increase_length(self):
        self.x.append(self.length)
        self.y.append(self.length)
        self.length += 1

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def go(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == "up":
            self.y[0] -= SQUARE
        if self.direction == "down":
            self.y[0] += SQUARE
        if self.direction == "left":
            self.x[0] -= SQUARE
        if self.direction == "right":
            self.x[0] += SQUARE

        self.draw()
