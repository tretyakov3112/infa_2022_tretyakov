import pygame
from pygame.draw import *
from random import randint

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

def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def new_balls():
    k = randint(1, 3)
    for i in range(k):
        new_ball()


def click(event):
    print(x, y, r)


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
            if isCaught(event, x, y, r):
                counter += 1
            # print('Click!', event.pos[0], event.pos[1], x, y, r)
    text_surface = my_font.render(f'COUNTER: {counter}', False, (255, 255, 255))
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
    screen.blit(text_surface, (50, 50))

pygame.quit()
