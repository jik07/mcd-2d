import os
import pygame
from start import start
from background import move_background
import pprint

width = 1000
height = int(width * 0.75)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

levels = []
for level in range(len(os.listdir('levels'))):
    with open('levels/lvl' + str(level) + '.txt', 'r') as f:
        tiles = [[int(tile) for tile in row.split()] for row in f.readlines()]
        levels.append(tiles)
pprint.pprint(levels)

level_l = len(levels[0])
levels = [[[pygame.transform.scale(pygame.image.load('textures/' + str(tile) + '.png').convert_alpha(), (height // level_l, height // level_l)) if tile > 0 else -1 for tile in row]
           for row in level]
           for level in levels]


level_position = [0, 0]
yChange = 0
ignore = False
s = -1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if s == -1:
        s = start(screen, 1000, s)

    screen.fill((51, 153, 255))

    current_level = levels[s]
    level_position, yChange, ignore = move_background(screen, current_level, level_position, yChange, ignore)

    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        level_position = [0, 0]
        yChange = 0
        ignore = False
        s = 1

    clock.tick(60)
