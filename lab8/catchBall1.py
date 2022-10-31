import time

import pygame
from pygame.draw import *
from random import randint
import time

pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

FPS = 1
screen = pygame.display.set_mode((1200, 900))

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
    __x = randint(100, 700)
    __y = randint(100, 500)
    __r = randint(30, 50)
    __v_x = 50
    __v_y = 50
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_r(self):
        return self.__r

    def get_v_x(self):
        return self.__v_x

    def get_v_y(self):
        return self.__v_y


    def new_moving_ball(self):
        '''рисует новый движущийся шарик '''

        self.__x += self.__v_x
        self.__y += self.__v_y

        color = COLORS[randint(0, 5)]
        circle(screen, color, (self.__x, self.__y), self.__r)


def isCaught(event, x, y, r):
    if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 < r ** 2:
        print('Caught!')
        return True
    else:
        return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # click(event)
            if isCaught(event, ball1.get_x(), ball1.get_y(), ball1.get_r()):
                counter += 1
            # print('Click!', event.pos[0], event.pos[1], x, y, r)
    text_surface = my_font.render(f'COUNTER: {counter}', False, (255, 255, 255))
    ball1 = Ball()
    # ball2 = Ball()
    ball1.new_moving_ball()

    # ball2.new_ball()
    pygame.display.update()
    screen.fill(BLACK)
    screen.blit(text_surface, (50, 50))

pygame.quit()
