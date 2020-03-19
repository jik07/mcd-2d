import pygame
from gui_elements import collision_test

def move_background(screen, scroll, level, player_rect, tiles, textures):

    scroll[0] += (player_rect.x-scroll[0] - 480)/20
    scroll[1] += (player_rect.y-scroll[1] - 355)/20
    scroll_int = scroll.copy()
    scroll_int[0] = int(scroll[0])
    scroll_int[1] = int(scroll[1])


    height = 75
    tile_rects = []
    y = 0
    # print("============START=============")
    for row in level:
        x = 0
        for tile in row:
            # print(tile)
            if tile != 0:

                screen.blit(textures[tile], (x * height - scroll_int[0], y * height - scroll_int[1]))
                tile_rects.append(pygame.Rect(x * height, y * height, height, height))
            x += 1
        y += 1

    return scroll, scroll_int, tile_rects
