import pygame

pygame.init()

# старт
size = (1200, 700)
sc = pygame.display.set_mode(size)
pygame.display.set_caption("Специальная теория относительности")

# colors
gold = (218, 165, 32)
red = (255, 0, 0)
green = (47, 79, 79)

# экран
sc.fill(green)

# slider
osn = pygame.Surface((200, 30))
polz = pygame.Surface((30, 30))

polz.fill((255, 0, 0))
osn.fill((0, 0, 255))

v = 0
x = 0
l = 0
osn.blit(polz, (x, 0))
sc.blit(osn, (500, 600))

# стержни
x_0 = 300  # натуральная длина
surf_l = pygame.Surface((x_0, 20))
surf_l.fill(gold)

l_s = 300  # длина, которую видим
surf_s = pygame.Surface((l_s, 20))
surf_s.fill(gold)

# шрифт
font = pygame.font.SysFont('timesnewroman', 32)

# надписи
follow = font.render('Специальная теория относительности', 1, gold)
nach_zn = font.render('1', 0, gold)
con_zn = font.render('300,000,000', 0, gold)
tec_zn = font.render(str(v), 0, gold)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            x, l = pygame.mouse.get_pos()
            x = x - 515
            if x > 170:
                x = 170
                v = x * 17647000
            elif x < 0:
                x = 0
                v = x * 17647000
            else:
                v = x * 17647000

    # экран
    sc.fill(green)

    # надписи
    sc.blit(follow, (350, 0))
    sc.blit(nach_zn, (480, 600))
    sc.blit(con_zn, (705, 600))

    # текущее значение скорости
    tec_zn = font.render(str(v), 0, gold)
    sc.blit(tec_zn, (600, 650))

    # меняю длину стержня
    surf_s = pygame.Surface((l_s, 20))
    surf_s.fill(gold)

    # рисую стержни
    sc.blit(surf_l, (50, 200))
    sc.blit(surf_s, (50, 500))

    # рисую линию
    pygame.draw.line(sc, gold, [0, 360], [1200, 360], 4)

    osn.fill((0, 0, 255))

    osn.blit(polz, (x, 0))
    sc.blit(osn, (500, 600))
    pygame.display.update()
    pygame.time.delay(100)
