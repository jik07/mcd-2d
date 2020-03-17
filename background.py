import pygame

def move_background(screen, picture, level_position, yChange, ignore):
    keys = pygame.key.get_pressed()

    if yChange == 0 and ignore == False:
        if keys[pygame.K_UP]:
            yChange = 10
    else:
        yChange -= 1
        if yChange == 0:
            ignore = True
        if yChange < -10:#currently, you can only stay at certain y. change this to set floor
            yChange = 0
            ignore = False

    speed = 0
    if keys[pygame.K_LEFT]:
        speed = 10
    elif keys[pygame.K_RIGHT]:
        speed = -10

    if yChange != 0 or (yChange == 0 and ignore == True):
        speed *= 1.25

    level_position[0] += speed
    level_position[1] += yChange

    screen.blit(picture, level_position)
    return level_position, yChange, ignore
