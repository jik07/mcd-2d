import os
import pygame
from start import start
from end import end
from background import move_background
from player import move_player
import pprint

width = 1000
height = int(width * 0.75)

pygame.init()
screen = pygame.display.set_mode((width, height))
player_img = pygame.image.load('potato.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (40, 40))

textures = [texture for texture in range(len(os.listdir('textures')) + 1)]
for texture in range(1, len(os.listdir('textures')) + 1):
    image = pygame.image.load('textures/' + str(texture) + '.png').convert_alpha()
    image = pygame.transform.scale(image, (40, 40))
    if texture == 5:
        image = pygame.transform.scale(image, (40, 30))
    textures[texture] = image

clock = pygame.time.Clock()

levels = []
for level in range(len(os.listdir('levels'))):
    with open('levels/lvl' + str(level) + '.txt', 'r') as f:
        tiles = [[int(tile) for tile in row.split()] for row in f.readlines()]
        levels.append(tiles)
# pprint.pprint(tiles)

scroll = [0, 0]
yChange = 0
xChange = 0
ignore = False
s = -1
player_rect = pygame.Rect(400, 0, 40, 40)
player_movement = [False, False, False]
running = True
while running:
    if s == -2:
        s = end(screen, 1000, s)
    if s == -1:
        s = start(screen, 1000, s)
    if s == -100:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((51, 153, 255))

    scroll, scroll_int, tile_rects, player_rect = move_background(screen, scroll, levels[s], player_rect, tiles, textures)
    player_rect, yChange, xChange, ignore, s = move_player(player_rect, yChange, xChange, ignore, tile_rects, player_movement, s)

    if s >= len(levels):
        s = -2

    screen.blit(player_img, (player_rect.x - scroll_int[0], player_rect.y - scroll_int[1]))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
