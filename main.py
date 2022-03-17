import pygame
import time
from const import *
from car import Car, ComputerCar
from gameInfo import GameInfo
from utils import blit_text_center

pygame.font.init()
MAIN_FONT = pygame.font.SysFont("comicsans", 44)
STAT_FONT = pygame.font.SysFont("comicsans", 30)

pygame.display.set_caption("Team Racing")

run = True
clock = pygame.time.Clock()

map_images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, (130, 250)), (TRACK_BORDER, (0, 0))]
player_car = Car(4, 4, RED_CAR, (180, 200))
computer_car = ComputerCar(4, 4, GREEN_CAR, (150, 200), PATH)
game_info = GameInfo()

while run:
    clock.tick((FPS))

    draw_images(WIN, map_images, player_car, computer_car)

    level_text = STAT_FONT.render(
        f"Level {game_info.level}", 1, (255, 255, 255))
    WIN.blit(level_text, (10, HEIGHT - level_text.get_height() - 70))

    time_text = STAT_FONT.render(
        f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
    WIN.blit(time_text, (8, HEIGHT - time_text.get_height() - 40))

    vel_text = STAT_FONT.render(
        f"Vel: {round(player_car.vel, 1)}px/s", 1, (255, 255, 255))
    WIN.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))

    pygame.display.update()

    while not game_info.started:
        blit_text_center(WIN, MAIN_FONT, f"Press ant key to start level {game_info.level}!")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                game_info.start_level()

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