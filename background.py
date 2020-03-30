import pygame
import pprint
from gui_elements import collision_test

def move_background(screen, scroll, level, player_rect, tiles, textures, spawn, d, through_door, s):

    scroll[0] += (player_rect.x-scroll[0] - 480)/20
    scroll[1] += (player_rect.y-scroll[1] - 355)/20
    scroll_int = scroll.copy()
    scroll_int[0] = int(scroll[0])
    scroll_int[1] = int(scroll[1])


    height = 40
    tile_rects = [[] for counter in range(len(tiles))]
    y = 0
    if not through_door[0]:
        d = -1
    num_d = 0
    # print("============START=============")
    for row in level:
        x = 0
        for tile in row:
            # print(tile)
            if tile == 5:
                screen.blit(textures[tile], (x * height - scroll_int[0], y * height - scroll_int[1] + 10))
                tile_rects[y].append([pygame.Rect(x * height, y * height + 25, height, 30), tile])
            elif tile == 6 or tile == 9:
                spawn[0] = x * height
                spawn[1] = y * height
                if tile == 6:
                    screen.blit(textures[tile], (x * height - scroll_int[0], y * height - scroll_int[1]))
                tile_rects[y].append([pygame.Rect(x * height, y * height, height, height), tile])
            elif tile == 7:
                rect = pygame.Rect(x * height, y * height, height*2, height*2)
                
                if s[1] == 0 and through_door[0]:
                    if d == num_d:
                        through_door[1] = rect.x + 20
                        through_door[2] = rect.y
                elif through_door[0]:
                    through_door[1] = rect.x + 20
                    through_door[2] = rect.y
                if player_rect.colliderect(rect) and player_rect.left > rect.left and player_rect.right < rect.right and not through_door[0]:
                    tex = 8
                    d = num_d
                else:
                    tex = 7
                screen.blit(textures[tex], (x * height - scroll_int[0], y * height - scroll_int[1]))
                tile_rects[y].append([rect, tile])
                num_d += 1
            else:
                if tile != 0:
                    screen.blit(textures[tile], (x * height - scroll_int[0], y * height - scroll_int[1]))
                tile_rects[y].append([pygame.Rect(x * height, y * height, height, height), tile])
            x += 1
        y += 1

    return scroll, scroll_int, tile_rects, player_rect, spawn, d, through_door
