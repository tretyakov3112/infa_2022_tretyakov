import numpy as np
import random
import pygame
from numpy import ndarray
from pygame.draw import *
import math
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

RED = (255, 0, 0)
BLUE = (0, 0, 255)

def rot(an, p0, p1):
    x1_rot = p0[0] + (p1[0] - p0[0]) * math.cos(an) - (p1[1] - p0[1]) * math.sin(an)
    y1_rot = p0[1] + (p1[0] - p0[0]) * math.sin(an) + (p1[1] - p0[1]) * math.cos(an)
    return np.array([x1_rot, y1_rot])

length = 50
width = 10
an = 1
p0 = np.array([200, 200])
p1 = p0 + np.array([length, 0])
p2 = p0 + np.array([0, width])

p1_rot: ndarray = rot(an, p0, p1)
p2_rot = rot(an, p0, p2)
p3_rot = p1_rot + p2_rot - p0




pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    polygon(screen, RED, [p2_rot, p0, p1_rot, p3_rot])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle(screen, RED, event.pos, 50)

                pygame.display.update()
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, 50)
                pygame.display.update()

pygame.quit()
