import pygame
width = 1000
height = int(width * 0.75)
screen = pygame.display.set_mode((width, height))


def text(text, color, size, x, y, centered = False, button = False, h = None):
    font = pygame.font.Font('paladins-font/PaladinsCondensed-rB77.otf', size)
    text = font.render(text, True, color)
    if button:
        y += (h - text.get_height()) / 2
    if centered:
        screen.blit(text, (width/2 - text.get_width() / 2, y))
    else:
        #width/2 makes the reference point of the text at the middle of the text
        screen.blit(text, (x - text.get_width()/2, y))#y remains the same = top of text


def button(t, x, y, w, h, ic, ac, cc, tc, ts):
    ret = True
    mouseX, mouseY = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    if x - w/2 < mouseX < x + w/2 and y < mouseY < y + h:
        pygame.draw.rect(screen, ac, (x - w/2, y, w, h))
        if click:
            pygame.draw.rect(screen, cc, (x - w/2, y, w, h))
            ret = False

    else:
        pygame.draw.rect(screen, ic, (x - w/2, y, w, h))
    text(t, tc, ts, x, y, False, True, h)
    return(ret)

def collision_test(rect, tiles):
    touching = []
    for row in tiles:
        for tile in row:
            if tile != -1:
                if rect.colliderect(tile.get_rect()):
                    touching.append(tile)
    return touching
