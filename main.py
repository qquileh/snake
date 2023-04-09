import pygame
from pygame.locals import *


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.body = pygame.image.load("images/body.jpg").convert()
        self.x = 250
        self.y = 250

    def draw(self):
        self.screen.fill((50, 240, 200))
        self.screen.blit(self.body, (self.x, self.y))
        pygame.display.update()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
        self.draw()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Snake")
        self.screen.fill((10, 200, 50))
        self.snake = Snake(self.screen)
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False



if __name__ == "__main__":
    game = Game()
    game.run()
