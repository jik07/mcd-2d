import pygame

def start(width):
    width = width
    height = int(width * 0.75)

    pygame.init()

    screen = pygame.display.set_mode((width, height))

    font = pygame.font.SysFont('dejavuserif', 72)
    text = font.render("Dungeon Adventure", True, (20, 0, 255))

    y = 200
    ySpeed = -10

    while True:
        pygame.time.wait(30)

        backgroundColor = (200, 0, 255)
        screen.fill(backgroundColor)
        screen.blit(text, (width/2 - text.get_width() // 2, 400))
        pygame.display.update()
