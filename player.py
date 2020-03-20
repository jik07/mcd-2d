import pygame
from gui_elements import collision_test

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
    if yChange > 18:
        yChange = 18

    if movement[0]:
        xChange = 5
    if movement[1]:
        xChange = -5
    if movement[2]:
        xChange *= 1.5



    player_rect.x += xChange
    collision_list = collision_test(player_rect,tiles)
    # print(collision_list)
    cl_count = 0
    for tile in collision_list:
        if xChange > 0:
            player_rect.right = tile.left
        if xChange < 0:
            player_rect.left = tile.right
    player_rect.y += yChange
    collision_list = collision_test(player_rect,tiles)
    # print(collision_list)
    for tile in collision_list:
        if yChange > 0:
            player_rect.bottom = tile.top
            yChange = 0
            ignore = False
            movement[2] = False
        if yChange < 0:
            player_rect.top = tile.bottom
            yChange = 0
            ignore = True


    return player_rect, yChange, ignore
