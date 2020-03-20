import pygame
from gui_elements import collision_test
import blocks

def move_player(player_rect, yChange, ignore, tiles, movement):

    xChange = 0
    movement[0] = False
    movement[1] = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        movement[0] = True
    if keys[pygame.K_LEFT]:
        movement[1] = True
    if keys[pygame.K_UP] and movement[2] == False:
        yChange = -10
        movement[2] = True

    yChange += 0.5
    if yChange == 0:
        ignore = True
    if yChange > 10:
        yChange = 10

    if movement[0]:
        xChange = 5
    if movement[1]:
        xChange = -5
    if movement[2]:
        xChange *= 1.5


    # Test horizontal collisions
    player_rect.x += xChange
    collision_list = collision_test(player_rect,tiles)
    for tile in collision_list:
        if tile[1] == 1 or tile[1] == 2: #grass or dirt
            blocks.dirt_grassH(xChange, player_rect, tile)

    # Test vertical collisions
    player_rect.y += yChange
    collision_list = collision_test(player_rect,tiles)
    for tile in collision_list:
        if tile[1] == 1 or tile[1] == 2: #grass or dirt
            blocks.dirt_grassV(yChange, player_rect, tile, ignore, movement)


    return player_rect, yChange, ignore
