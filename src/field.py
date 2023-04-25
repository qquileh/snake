import pygame


class Field:
    def __init__(self, screen, num_of_squares):
        if num_of_squares == 19:
            self.body = pygame.image.load("images/pix760.jpg").convert()
        elif num_of_squares == 17:
            self.body = pygame.image.load("images/pix680.jpg").convert()
        elif num_of_squares == 15:
            self.body = pygame.image.load("images/pix600.jpg").convert()

        self.screen = screen
        self.x = 0
        self.y = 0

    def draw(self):
        self.screen.blit(self.body, (self.x, self.y))
        pygame.display.update()
