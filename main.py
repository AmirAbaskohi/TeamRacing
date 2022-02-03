import pygame
import time
from const import *
from car import Car

pygame.display.set_caption("Team Racing")

run = True
clock = pygame.time.Clock()

map_images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
player_car = Car(4, 4, RED_CAR, (180, 200))

while run:
    clock.tick((FPS))

    WIN.blit(GRASS, (0, 0))
    WIN.blit(TRACK, (0, 0))

    draw_images(WIN, map_images, player_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    is_moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        is_moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        is_moved = True
        player_car.move_backward()

    if not is_moved:
        player_car.reduce_speed()

pygame.quit()