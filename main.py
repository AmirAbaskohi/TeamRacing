import pygame
import time
from const import *
from car import Car, ComputerCar

pygame.display.set_caption("Team Racing")

run = True
clock = pygame.time.Clock()

map_images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, (130, 250)), (TRACK_BORDER, (0, 0))]
player_car = Car(4, 4, RED_CAR, (180, 200))
computer_car = ComputerCar(4, 4, GREEN_CAR, (150, 200), PATH)

while run:
    clock.tick((FPS))

    WIN.blit(GRASS, (0, 0))
    WIN.blit(TRACK, (0, 0))

    draw_images(WIN, map_images, player_car, computer_car)

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

    computer_car.move()

    if not is_moved:
        player_car.reduce_speed()

    if player_car.collide(TRACK_BORDER_MASK) != None:
        player_car.bounce()

    player_finish_poi_collide = player_car.collide(FINISH_MASK, 130, 250)
    computer_finish_poi_collide = computer_car.collide(FINISH_MASK, 130, 250)
    if computer_finish_poi_collide != None:
        player_car.reset()
        computer_car.reset()
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            player_car.reset()
            computer_car.reset()

pygame.quit()