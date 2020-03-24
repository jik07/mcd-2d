import pygame
from gui_elements import collision_test
import blocks

def move_player(player_rect, yChange, xChange, ignore, tiles, movement, s):


    keys = pygame.key.get_pressed()
    movement[0] = False
    movement[1] = False
    if yChange != 0:
        movement[2] = True
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
    if yChange > 18:
        yChange = 18

    if movement[2] == False:
        xChange = 0
        if movement[0]:
            xChange = 5
        if movement[1]:
            xChange = -5

    else:
        if movement[0]:
            xChange += 1
        if movement[1]:
            xChange -= 1
        if xChange > 0:
            xChange -= 0.5
        if xChange < 0:
            xChange += 0.5
        if xChange > 8:
            xChange = 8
        if xChange < -8:
            xChange = -8



    # Test horizontal collisions
    player_rect.x += xChange
    collision_list = collision_test(player_rect,tiles)
    for tile in collision_list:
        if tile[1] == 1 or tile[1] == 2: #grass or dirt
            xChange, yChange, player_rect, tile, ignore = blocks.dirt_grass(True, xChange, yChange, player_rect, tile, movement, ignore)
        if tile[1] == 3:
            player_rect, s = blocks.portal(player_rect, s)
        if tile[1] == 4:
            player_rect = blocks.lava(player_rect)

    # Test vertical collisions
    player_rect.y += yChange
    collision_list = collision_test(player_rect,tiles)
    for tile in collision_list:
        if tile[1] == 1 or tile[1] == 2: #grass or dirt
            xChange, yChange, player_rect, tile, ignore = blocks.dirt_grass(False, xChange, yChange, player_rect, tile, movement, ignore)
        if tile[1] == 3:
            player_rect, s = blocks.portal(player_rect, s)
        if tile[1] == 4:
            player_rect = blocks.lava(player_rect)

    return player_rect, yChange, xChange, ignore, s
