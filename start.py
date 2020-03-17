import pygame
import gui_elements

def start(width, screenvar):
    width = width
    height = int(width * 0.75)
    running = True

    pygame.init()
    screen = pygame.display.set_mode((width, height))

    while running:
        pygame.time.wait(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                screenvar = False
                return(screenvar)
        backgroundColor = (200, 0, 255)
        screen.fill(backgroundColor)
        gui_elements.text("Dungeon Adventure", (102, 0, 204), 72, 0, 200, True)
        running = gui_elements.button("Start!", 500, 500, 400, 60, (204, 0 , 204), (255, 51, 255), (153, 0, 153), (102, 0, 204), 72)
        if not running:
            screenvar = 0
            return(screenvar)
        pygame.display.update()
