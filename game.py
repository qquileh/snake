import pygame
import time
from snake import Snake
from apple import Apple
from pygame.locals import KEYDOWN, K_SPACE, K_ESCAPE, K_q, K_UP, K_DOWN, K_RIGHT, K_LEFT, QUIT

SQUARE = 40
LOSE_BACKGROUND = (255, 0, 0)
BACKGROUND = (50, 240, 200)
FIELD_SIZE = 800
DEFAULT_SPEED = 0.4


class Game:
    def __init__(self):
        self.speed = DEFAULT_SPEED
        self.start_time = time.time()
        pygame.init()
        self.screen = pygame.display.set_mode((FIELD_SIZE, FIELD_SIZE))
        pygame.display.set_caption("Snake")
        self.screen.fill(BACKGROUND)
        self.snake = Snake(self.screen, 1)
        self.apple = Apple(self.screen)

    def reset(self):
        self.snake = Snake(self.screen, 1)
        self.apple = Apple(self.screen)
        self.speed = DEFAULT_SPEED

    def show_score(self):
        font = pygame.font.SysFont('calibri', 20)
        score = font.render(f"Счёт: {self.snake.length}", True, (0, 0, 0))
        self.screen.blit(score, (15, 15))
        pygame.display.update()

    def check_if_eat_apple(self):
        if self.is_contact(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

    def check_if_eat_snake(self):
        for i in range(1, self.snake.length):
            if self.is_contact(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise BaseException

    def check_if_eat_border(self):
        if not (0 <= self.snake.x[0] < FIELD_SIZE and 0 <= self.snake.y[0] < FIELD_SIZE):
            raise BaseException

    def update_speed(self):
        current_time = time.time()
        dif = current_time - self.start_time
        if dif > 3:
            self.speed /= 1.5
            self.start_time = current_time

    def game_on(self):
        self.update_speed()
        self.snake.go()
        self.check_if_eat_apple()
        self.check_if_eat_snake()
        self.check_if_eat_border()
        self.apple.draw()
        self.show_score()

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pause = False

                    elif event.key == K_ESCAPE:
                        pause = True

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
                else:
                    self.start_time = time.time()

            except BaseException:
                self.game_over()
                pause = True
                self.reset()

            time.sleep(self.speed)
        else:
            self.game_over()

    def is_contact(self, x_1, y_1, x_2, y_2):
        if x_1 == x_2:
            if y_1 == y_2:
                return True
        return False

    def game_over(self):
        self.screen.fill(LOSE_BACKGROUND)
        font = pygame.font.SysFont('calibri', 30)
        game_over = font.render(f"Игра окончена. Ваш счёт: {self.snake.length}", True, (0, 0, 0))
        self.screen.blit(game_over, (15, 40))
        play_again = font.render("Нажмите 'пробел', чтобы играть снова", True, (0, 0, 0))
        self.screen.blit(play_again, (15, 80))
        pygame.display.update()
