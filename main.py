import pygame
from start import start
from background import move_background

width = 1000
height = int(width * 0.75)

pygame.init()
screen = pygame.display.set_mode((width, height))

start(screen, width, height)
#current level = start_screen(blahblahblah)

#test image level
current_level = pygame.transform.scale(
    pygame.image.load('levels/test.png').convert_alpha(),
    (width, height))

level_position = [0, 0]
yChange = 0
running = True
ignore = False
while running:
    pygame.time.wait(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    level_position, yChange, ignore = move_background(screen, current_level, level_position, yChange, ignore)

    pygame.display.update()
