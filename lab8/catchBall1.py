import time

import pygame
from pygame.draw import *
from random import randint
from random import choice
import time

pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

FPS = 30
WIDTH = 1000
HIGHT = 700
screen = pygame.display.set_mode((WIDTH, HIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
counter = 0


class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 10
        self.vy = 10
        self.color = choice(COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self):
        """Функция проверяет, сталкивалкивается ли шарик со стеной.

        Returns:
            Возвращает True в случае столкновения мяча и стены. В противном случае возвращает False.
        """
        delta = 10*(self.vx+self.vy)/FPS
        if (self.y > self.r + delta) and (self.y < HIGHT - self.r - delta) and (self.x > self.r + delta) and (self.x < WIDTH - self.r - delta):
            return False
        else:
            return True

    def fix_position(self):
        if (self.x < 1+self.r):
            self.x = 1+self.r
        if (self.x > WIDTH-self.r-1):
            self.x = WIDTH-self.r-1
        if (self.y < 1+self.r):
            self.y = 1+self.r
        if (self.y > HIGHT-self.r-1):
            self.y = HIGHT-self.r-1

    def rand_v(self):
        if self.vx < 0:
            if self.vy < 0:
                self.vx = randint(1, 10)
                self.vy = randint(1, 10)
            else:
                self.vx = randint(1, 10)
                self.vy = randint(1, 10) - 12
        else:
            if self.vy < 0:
                self.vx = randint(1, 10) - 12
                self.vy = randint(1, 10)
            else:
                self.vx = randint(1, 10) - 12
                self.vy = randint(1, 10) - 12

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_r(self):
        return self.r

    def get_v_x(self):
        return self.v_x

    def get_v_y(self):
        return self.v_y


def isCaught(event, x, y, r):
    if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 < r ** 2:
        print('Caught!')
        return True
    else:
        return False


pygame.display.update()

clock = pygame.time.Clock()
finished = False
ball = Ball(screen, 200, 200)
while not finished:
    clock.tick(FPS)

    ball.draw()
    if ball.hittest():
        ball.fix_position()
        ball.rand_v()
    # ball1 = Ball(300, 300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if isCaught(event, ball.get_x(), ball.get_y(), ball.get_r()):
                counter += 1

    text_surface = my_font.render(f'COUNTER: {counter}', False, (255, 255, 255))

    # ball2 = Ball()
    ball.move()

    # ball2.new_ball()
    pygame.display.update()
    screen.fill(BLACK)
    screen.blit(text_surface, (50, 50))

pygame.quit()
