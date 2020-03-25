import pygame
import pprint
from gui_elements import collision_test

def move_background(screen, scroll, level, player_rect, tiles, textures, spawn):

    scroll[0] += (player_rect.x-scroll[0] - 480)/20
    scroll[1] += (player_rect.y-scroll[1] - 355)/20
    scroll_int = scroll.copy()
    scroll_int[0] = int(scroll[0])
    scroll_int[1] = int(scroll[1])


    height = 40
    tile_rects = [[] for counter in range(len(tiles))]
    y = 0
    # print("============START=============")
    for row in level:
        x = 0
        for tile in row:
            # print(tile)
            if tile == 5:
                print("y")
                screen.blit(textures[tile], (x * height - scroll_int[0], y * height - scroll_int[1] + 25))
                tile_rects[y].append([pygame.Rect(x * height, y * height + 25, height, 30), tile])
            if tile == 6:
                spawn[0] = x * height
                spawn[1] = y * height
                screen.blit(textures[tile], (x * height - scroll_int[0], y * height - scroll_int[1]))
                tile_rects[y].append([pygame.Rect(x * height, y * height, height, height), tile])
            else:
                if tile != 0:
                    screen.blit(textures[tile], (x * height - scroll_int[0], y * height - scroll_int[1]))
                tile_rects[y].append([pygame.Rect(x * height, y * height, height, height), tile])
            x += 1
        y += 1
    if player_rect.y > 700:
        player_rect.x, player_rect.y = spawn[0], spawn[1]
    return scroll, scroll_int, tile_rects, player_rect, spawn
