import pygame
import time
from snake import Snake
from apple import Apple
from field import Field
from pygame.locals import KEYDOWN, K_SPACE, K_ESCAPE, K_UP, K_DOWN, K_RIGHT, K_LEFT, QUIT, K_1, K_2, K_3, K_m, K_t

SQUARE = 40
LOSE_BACKGROUND = (255, 0, 0)
BACKGROUND = (50, 240, 200)
SCREEN_SIZE = 800
DEFAULT_SPEED = 0.4
INDENT = 10


class Game:
    def __init__(self):
        self.start_time = time.time()
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Snake")
        self.screen.fill(BACKGROUND)
        self.num_of_squares = 19
        self.level = 1
        self.snake = Snake(self.screen, length=1)
        self.apple = Apple(self.screen, num_of_squares=self.num_of_squares)
        self.field = Field(self.screen, num_of_squares=self.num_of_squares)
        self.speed = DEFAULT_SPEED
        self.attempt = self.get_attempt()
        pygame.display.update()
        self.game_menu()

    def get_attempt(self):
        with open('number_of_attempts.txt') as f:
            attempt = int(f.read())
            return attempt

    def reset(self, num, lvl):
        self.screen.fill(BACKGROUND)
        self.num_of_squares = num
        self.level = lvl
        self.snake = Snake(self.screen, length=1)
        self.apple = Apple(self.screen, num_of_squares=self.num_of_squares)
        self.field = Field(self.screen, num_of_squares=self.num_of_squares)
        self.speed = DEFAULT_SPEED
        self.attempt += 1
        pygame.display.update()

    def game_menu(self):
        self.screen.fill(BACKGROUND)
        font = pygame.font.SysFont('calibri', 30)
        menu_message = font.render("Выберите уровень, нажав 1, 2 или 3 на клавиатуре", True, (0, 0, 0))
        self.screen.blit(menu_message, (15, 40))
        records_message = font.render("Нажмите 't', чтобы увидеть таблицу рекордов", True, (0, 0, 0))
        self.screen.blit(records_message, (15, 80))
        pygame.display.update()

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
        field_size = self.num_of_squares * SQUARE
        if not (INDENT <= self.snake.x[0] < INDENT + field_size and INDENT <= self.snake.y[0] < INDENT + field_size):
            raise BaseException

    def update_speed(self):
        current_time = time.time()
        dif = current_time - self.start_time
        if dif > 3:
            self.speed /= 1.2
            self.start_time = current_time

    def game_on(self):
        self.update_speed()
        self.field.draw()
        self.snake.go()
        self.check_if_eat_apple()
        self.check_if_eat_snake()
        self.check_if_eat_border()
        self.apple.draw()
        self.show_score()

    def run(self):
        running = True
        pause = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pause = False

                    elif event.key == K_m:
                        self.game_menu()

                    elif event.key == K_t:
                        self.show_records()

                    elif event.key == K_ESCAPE:
                        pause = True

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

                    elif event.key == K_1:
                        self.reset(19, 1)
                        pause = False

                    elif event.key == K_2:
                        self.reset(17, 2)
                        pause = False

                    elif event.key == K_3:
                        self.reset(15, 3)
                        pause = False

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

            time.sleep(self.speed)
        '''
        else:
            self.clear_results()
        '''

    '''
    def clear_results(self):
        for i in range(1, 4):
            with open(f'records_{i}.txt', 'w'):
                continue
    '''

    def is_contact(self, x_1, y_1, x_2, y_2):
        if x_1 == x_2:
            if y_1 == y_2:
                return True
        return False

    def show_records(self):
        self.screen.fill(BACKGROUND)
        font = pygame.font.SysFont('calibri', 30)
        coordinate_attempt = 70
        coordinate_level = 40
        for i in range(3):
            message = font.render(f"Рекорды уровня {i + 1}", True, (0, 0, 0))
            self.screen.blit(message, (15, coordinate_level))
            with open(f'records_{i + 1}.txt') as f:
                lines = f.readlines()
                lines = [line.rstrip() for line in lines]
                to_print = 5
                length = len(lines)
                if length < to_print:
                    to_print = length
                for i in range(to_print):
                    message = font.render(lines[i], True, (0, 0, 0))
                    self.screen.blit(message, (15, coordinate_attempt))
                    coordinate_attempt += 30
            coordinate_level += 240
            coordinate_attempt = coordinate_level + 30
        message = font.render("Нажмите 'm', чтобы выйти в меню", True, (0, 0, 0))
        self.screen.blit(message, (15, coordinate_level))
        pygame.display.update()

    def update_records(self):
        attempts = [(f"attempt#{self.attempt}:", self.snake.length)]
        with open(f'records_{self.level}.txt') as f:
            lines = f.readlines()
            for i in lines:
                attempts.append((i.split()[0], int(i.split()[1])))
        attempts.sort(key=lambda x: x[1], reverse=True)

        length = len(attempts)
        with open(f'records_{self.level}.txt', 'w') as f:
            for i in range(length):
                f.write(f"{attempts[i][0]} {attempts[i][1]}\n")

    def update_attempts(self):
        with open('number_of_attempts.txt', 'w') as f:
            f.write(str(self.attempt))

    def game_over(self):
        self.update_records()
        self.update_attempts()
        self.screen.fill(LOSE_BACKGROUND)
        font = pygame.font.SysFont('calibri', 30)
        your_score = font.render(f"Игра окончена. Ваш счёт: {self.snake.length}", True, (0, 0, 0))
        self.screen.blit(your_score, (15, 40))
        your_attempt = font.render(f"Ваша попытка: attempt#{self.attempt}", True, (0, 0, 0))
        self.screen.blit(your_attempt, (15, 80))
        play_again = font.render("Нажмите 'm', чтобы выйти в меню", True, (0, 0, 0))
        self.screen.blit(play_again, (15, 120))
        pygame.display.update()
