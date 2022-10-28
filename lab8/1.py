import pygame
from pygame.draw import *

pygame.init()
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

FPS = 30
size = 600
screen = pygame.display.set_mode((size, size))

circle(screen, YELLOW, (size//2, size//2), size//3)
circle(screen, BLACK, (size//2, size//2), size//3, 5)
circle(screen, RED, (0.35*size, 0.4*size), 0.1*size)
circle(screen, RED, (0.65*size, 0.4*size), 0.07*size)
circle(screen, BLACK, (0.35*size, 0.4*size), 0.06*size)
circle(screen, BLACK, (0.65*size, 0.4*size), 0.03*size)
polygon(screen, BLACK, [(0.3*size, 0.6*size), (0.3*size, 0.65*size),  (0.7*size, 0.65*size), (0.7*size, 0.6*size)])
polygon(screen, BLACK, [(0.2*size, 0.19*size), (0.18*size, 0.21*size),  (0.45*size, 0.34*size), (0.47*size, 0.32*size)])
polygon(screen, BLACK, [((1-0.2)*size, 0.22*size), ((1-0.18)*size, 0.24*size),  ((1-0.45)*size, 0.37*size), ((1-0.47)*size, 0.35*size)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()