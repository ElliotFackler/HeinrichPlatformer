# This is a sample Python script.
import pygame, sys
from settings import *
from tile import Tile
from level import Level
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()


    pygame.display.update()
    clock.tick(60)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
