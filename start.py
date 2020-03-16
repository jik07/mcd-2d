import pygame

def start(width):
    width = width
    height = int(width * 0.75)

    pygame.init()

    screen = pygame.display.set_mode((width, height))

    def text(text, color, size, x, y, centered = False, button = False, h = None):
        font = pygame.font.SysFont('dejavuserif', size)
        text = font.render(text, True, color)
        if button:
            y += (h - text.get_height()) / 2
        if centered:
            screen.blit(text, (width/2 - text.get_width() / 2, y))
        else:
            #width/2 makes the reference point of the text at the middle of the text
            screen.blit(text, (x - text.get_width()/2, y))#y remains the same = top of text


    def button(t, x, y, w, h, ic, ac, cc, tc, ts):
        mouseX, mouseY = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        if x - w/2 < mouseX < x + w/2 and y < mouseY < y + h:
            pygame.draw.rect(screen, ac, (x - w/2, y, w, h))
            if click:
                pygame.draw.rect(screen, cc, (x - w/2, y, w, h))
        else:
            pygame.draw.rect(screen, ic, (x - w/2, y, w, h))
        text(t, tc, ts, x, y, False, True, h)


    running = True
    while running:
        pygame.time.wait(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        backgroundColor = (200, 0, 255)
        screen.fill(backgroundColor)
        text("Dungeon Adventure", (102, 0, 204), 72, 0, 400, True)
        button("Start!", 500, 500, 200, 60, (204, 0 , 204), (255, 51, 255), (153, 0, 153), (102, 0, 204), 72)
        pygame.display.update()
