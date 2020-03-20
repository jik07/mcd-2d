import pygame
import gui_elements

def start(screen, width, screenvar):
    width = width
    height = int(width * 0.75)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        pygame.time.wait(30)
        backgroundColor = (200, 0, 255)
        screen.fill(backgroundColor)
        gui_elements.text("Dungeon Adventure", (102, 0, 204), 72, 0, 200, True)

        if not gui_elements.button("Start!", 500, 500, 400, 60, (204, 0 , 204), (255, 51, 255), (153, 0, 153), (102, 0, 204), 72):
            screenvar = 0
            print(f"screenvar: {screenvar}")
            return screenvar
            break


        pygame.display.update()
