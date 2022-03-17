import pygame
from utils import *

GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)

TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

FINISH = pygame.image.load("imgs/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Team Racing")

FPS = 60

PATH = [(176, 136), (126, 68), (59, 143), (62, 467), (350, 733), (408, 669), (419, 516), (504, 470), (594, 529), (614, 705), (733, 710), (743, 422), (678, 364), (418, 357), (395, 311), (441, 263), (703, 258), (741, 175), (709, 79), (310, 81), (284, 145), (288, 361), (234, 416), (171, 366), (172, 260)]