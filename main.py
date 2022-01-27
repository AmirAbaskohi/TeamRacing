import pygame
import time
import math
from const import *

pygame.display.set_caption("Team Racing")

run = True
clock = pygame.time.Clock()

images = [(GRASS, (0, 0)), (TRACK, (0, 0))]

while run:
    clock.tick((FPS))

    WIN.blit(GRASS, (0, 0))
    WIN.blit(TRACK, (0, 0))

    draw_images(WIN, images)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()