import pygame
import random

SQUARE = 40
NUM_OF_SQUARES = 20


class Apple:
    def __init__(self, screen):
        self.body = pygame.image.load("images/apple.jpg").convert()
        self.screen = screen
        self.x = random.randint(0, NUM_OF_SQUARES - 1) * SQUARE
        self.y = random.randint(0, NUM_OF_SQUARES - 1) * SQUARE

    def draw(self):
        self.screen.blit(self.body, (self.x, self.y))
        pygame.display.update()

    def move(self):
        self.x = random.randint(0, NUM_OF_SQUARES - 1) * SQUARE
        self.y = random.randint(0, NUM_OF_SQUARES - 1) * SQUARE
