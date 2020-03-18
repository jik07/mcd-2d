import pygame
from gui_elements import collision_test

def move_background(screen, scroll, level, player_rect, tiles):

    scroll[0] += (player_rect.x-scroll[0] - 480)/20
    scroll[1] += (player_rect.y-scroll[1] - 355)/20
    scroll_int = scroll.copy()
    scroll_int[0] = int(scroll[0])
    scroll_int[1] = int(scroll[1])


    height = 75
    tile_rects = []
    y = 0
    row_count = 0
    for row in level:
        x = 0
        tile_count = 0
        for tile in row:
            if tile != 0:
                image = pygame.image.load('textures/' + str(tile) + '.png').convert_alpha()
                image = pygame.transform.scale(image, (height, height))
                screen.blit(image, (x * height - scroll_int[0], y * height - scroll_int[1]))
                tile_rects.append([pygame.Rect(x * height, y * height, height, height), tiles[row_count][tile_count]])
            x += 1
            tile_count += 1
        y += 1
        row_count += 1

    return scroll, scroll_int, tile_rects
