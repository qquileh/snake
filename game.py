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

    def reset(self):
        self.snake = Snake(self.screen, 1)
        self.apple = Apple(self.screen)

    def show_score(self):
        font = pygame.font.SysFont('calibri', 20)
        score = font.render(f"Счёт: {self.snake.length}", True, (0, 0, 0))
        self.screen.blit(score, (15, 15))

    def check_if_eat_apple(self):
        if self.is_contact(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

    def check_if_eat_snake(self):
        for i in range(3, self.snake.length):
            if self.is_contact(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Ate myself"

    def check_if_eat_border(self):
        if not (0 <= self.snake.x[0] < 800 and 0 <= self.snake.y[0] < 800):
            raise "Ate border"

    def game_on(self):
        self.snake.go()
        self.apple.draw()
        self.show_score()
        pygame.display.update()
        self.check_if_eat_apple()
        self.check_if_eat_snake()
        self.check_if_eat_border()

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pause = False

                    elif event.key == K_q:
                        running = False

                    elif event.key == K_UP:
                        if self.snake.direction == "left" or self.snake.direction == "right":
                            self.snake.move_up()

                    elif event.key == K_DOWN:
                        if self.snake.direction == "left" or self.snake.direction == "right":
                            self.snake.move_down()

                    elif event.key == K_LEFT:
                        if self.snake.direction == "up" or self.snake.direction == "down":
                            self.snake.move_left()

                    elif event.key == K_RIGHT:
                        if self.snake.direction == "up" or self.snake.direction == "down":
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.game_on()

            except Exception:
                self.game_over()
                pause = True
                self.reset()

            time.sleep(0.5)
        else:
            self.game_over()


    def is_contact(self, x_1, y_1, x_2, y_2):
        if x_1 == x_2:
            if y_1 == y_2:
                return True
        return False

    def game_over(self):
        self.screen.fill((10, 200, 50))
        font = pygame.font.SysFont('calibri', 30)
        game_over = font.render(f"Игра окончена. Ваш счёт: {self.snake.length}", True, (0, 0, 0))
        self.screen.blit(game_over, (300, 400))
        play_again = font.render("Нажмите 'пробел', чтобы играть снова", True, (0, 0, 0))
        self.screen.blit(play_again, (300, 440))
        pygame.display.update()
