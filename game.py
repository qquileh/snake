import pygame
import time
from snake import Snake
from apple import Apple
from pygame.locals import *

SQUARE = 40


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Snake")
        self.screen.fill((10, 200, 50))
        self.snake = Snake(self.screen, 1)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()


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

            self.snake.go()
            self.apple.draw()
            if self.is_eating_apple(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                self.snake.increase_length()
                self.apple.move()

            time.sleep(0.2)

    def is_eating_apple(self, x_1, y_1, x_2, y_2):
        if x_1 >= x_2 and x_1 < x_2 + SQUARE:
            if y_1 >= y_2 and y_1 < y_2 + SQUARE:
                return True
        return False


