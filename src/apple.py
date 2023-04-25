import pygame
import random

SQUARE = 40
INDENT = 10


class Apple:
    def __init__(self, screen, num_of_squares):
        self.num_of_squares = num_of_squares
        self.body = pygame.image.load("images/apple.jpg").convert()
        self.screen = screen
        self.x = INDENT + random.randint(0, self.num_of_squares - 1) * SQUARE
        self.y = INDENT + random.randint(0, self.num_of_squares - 1) * SQUARE

    def draw(self):
        self.screen.blit(self.body, (self.x, self.y))
        pygame.display.update()

    def move(self):
        self.x = INDENT + random.randint(0, self.num_of_squares - 1) * SQUARE
        self.y = INDENT + random.randint(0, self.num_of_squares - 1) * SQUARE
