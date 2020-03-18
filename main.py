import os
import pygame
from start import start
from background import move_background
from player import move_player
import pprint

width = 1000
height = int(width * 0.75)

pygame.init()
screen = pygame.display.set_mode((width, height))
player_img = pygame.image.load('potato.png').convert()
player_img = pygame.transform.scale(player_img, (40, 40))

clock = pygame.time.Clock()

levels = []
for level in range(len(os.listdir('levels'))):
    with open('levels/lvl' + str(level) + '.txt', 'r') as f:
        tiles = [[int(tile) for tile in row.split()] for row in f.readlines()]
        levels.append(tiles)
pprint.pprint(tiles)

scroll = [0, 0]
yChange = 0
ignore = False
s = -1
player_rect = pygame.Rect(500, 300, 40, 40)
player_movement = [False, False, False]
running = True
while running:
    if s == -1:
        s = start(screen, 1000, s)
        print(s)
    if s == -100:
        running = False
        print(s)
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((51, 153, 255))

    scroll, scroll_int, tile_rects = move_background(screen, scroll, levels[s], player_rect, tiles)
    player_rect, yChange, ignore = move_player(player_rect, yChange, ignore, tile_rects, player_movement)

    screen.blit(player_img, (player_rect.x - scroll_int[0], player_rect.y - scroll_int[1]))
    pygame.display.update()

    clock.tick(60)

pygame.quit()
