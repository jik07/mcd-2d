import pygame

pygame.init()
r = 0
colorSpeed = 0.2
switch = True
screen = pygame.display.set_mode((800, 600))


def loadify(imgname):
    return pygame.image.load(imgname).convert_alpha()


font = pygame.font.SysFont('dejavuserif', 72)
text = font.render("Laggy Patatas!", True, (0, 128, 0))
potatoImg = loadify('unnamed.png')
y = 200
ySpeed = -10


def potato(x, y):
    screen.blit(potatoImg, (x, y))


clock = pygame.time.Clock()
while True:
    pygame.time.wait(30)
    # t = (0, 0, 0)
    # pygame.event.get()
    # if pygame.mouse.get_pressed() != t:
    #     print(pygame.mouse.get_pressed())
    colorSpeed = (256 ** 2 - r ** 2) / 45000
    if switch:
        r += colorSpeed
    if r >= 255:
        r = 255
        switch = False
    else:
        r -= colorSpeed
        if r <= 0:
            r = 0
            switch = True
    y += ySpeed
    ySpeed += 1
    if ySpeed > 10:
        ySpeed = -10
    backgroundColor = (r, 255, 0)
    screen.fill(backgroundColor)
    screen.blit(text, (400 - text.get_width() // 2, 400))
    potato(300, y)
    pygame.display.flip()
    clock.tick(30)