import pygame

def move_background(screen, tiles, level_position, yChange, ignore):
    pw = 30
    px = (1000/2)-(pw/2)
    py = (1000/2)-(pw/2)
    player = pygame.Rect(px, py, pw, pw)

    keys = pygame.key.get_pressed()

    if yChange == 0 and ignore == False:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            yChange = 10
    else:
        yChange -= 0.5
        if yChange == 0:
            ignore = True
        if yChange < -10:#currently, you can only stay at certain y. change this to set floor
            yChange = 0
            ignore = False


    speed = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        speed = 5
    if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
        speed = -5

    if yChange != 0 or (yChange == 0 and ignore == True) or keys[pygame.K_UP] or keys[pygame.K_w]:
        speed *= 1.5

    level_position[0] += speed
    level_position[1] += yChange

    for row in tiles:
        for tile in row:
            if tile != -1:
                screen.blit(tile, (row.index(tile) * tile.get_height() + level_position[0], tiles.index(row) * tile.get_height() + level_position[1]))

    pygame.draw.rect(screen, (0, 0, 0), player)
    return level_position, yChange, ignore
