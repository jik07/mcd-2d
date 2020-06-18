import pygame
from gui_elements import collision_test
import blocks

def move_player(player_rect, yChange, xChange, ignore, tiles, movement, s, spawn, new_level, d, through_door):
    if new_level:
        player_rect.x, player_rect.y = spawn[0], spawn[1]
        new_level = False
    if through_door[0]:
        through_door[0] = False
        player_rect.x, player_rect.y = through_door[1], through_door[2]

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

    movement[3] = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                movement[3] = True

    yChange += 0.5
    if yChange == 0:
        ignore = True
    if yChange > 18:
        yChange = 18

    if movement[2] == False:
        xChange = 0
        if movement[0] and movement[1]:
            xChange = 0
        else:
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
        if xChange > 7.5:
            xChange = 8
        if xChange < -8:
            xChange = -7.5

    # Test horizontal collisions
    player_rect.x += xChange
    collision_list = collision_test(player_rect,tiles)
    for tile in collision_list:
        if tile[1] == 1 or tile[1] == 2: #grass or dirt
            xChange, yChange, player_rect, tile, ignore = blocks.dirt_grass(True, xChange, yChange, player_rect, tile, movement, ignore)
        if tile[1] == 3:
            player_rect, s, new_level, yChange, xChange, ignore = blocks.portal(player_rect, s, new_level, yChange, xChange, ignore)
        if tile[1] == 4 or tile[1] == 5:
            player_rect, yChange, xChange, ignore = blocks.lava(player_rect, spawn, yChange, xChange, ignore)
        if tile[1] == 7 and player_rect.left > tile[0].left and player_rect.right < tile[0].right:
            player_rect, s, d = blocks.door(player_rect, s, d, movement, through_door)


    # Test vertical collisions
    player_rect.y += yChange
    collision_list = collision_test(player_rect,tiles)
    for tile in collision_list:
        if tile[1] == 1 or tile[1] == 2: #grass or dirt
            xChange, yChange, player_rect, tile, ignore = blocks.dirt_grass(False, xChange, yChange, player_rect, tile, movement, ignore)
        if tile[1] == 3:
            player_rect, s, new_level, yChange, xChange, ignore = blocks.portal(player_rect, s, new_level, yChange, xChange, ignore)
        if tile[1] == 4 or tile[1] == 5:
            player_rect, yChange, xChange, ignore = blocks.lava(player_rect, spawn, yChange, xChange, ignore)
        if tile[1] == 8:
            player_rect, s, d = blocks.door(player_rect, s, d, movement, through_door)

    if player_rect.y > 700:
        player_rect.x, player_rect.y = spawn[0], spawn[1]

    return player_rect, yChange, xChange, ignore, s, new_level, movement, through_door, d
