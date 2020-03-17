import pygame
from start import start
from background import move_background

width = 1000
height = int(width * 0.75)

pygame.init()
screen = pygame.display.set_mode((width, height))

levels = ['levels/test.png']
levels = [pygame.image.load(x).convert_alpha() for x in levels]
levels = [pygame.transform.scale(x,(int(x.get_width()/x.get_height() * height), height)) for x in levels]

level_position = [0, 0]
yChange = 0
running = True
ignore = False
s = -1
running = True
while running:
    pygame.time.wait(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if s == -1:
        s = start(1000, s)

    current_level = levels[s]
    screen.fill((0, 0, 0))
    level_position, yChange, ignore = move_background(screen, current_level, level_position, yChange, ignore)

    pygame.display.update()
