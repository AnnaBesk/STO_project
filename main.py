import pygame
import math

pygame.init()

# старт
size = (1200, 700)
sc = pygame.display.set_mode(size)
pygame.display.set_caption("Специальная теория относительности")

# colors
gold = (218, 165, 32)
red = (255, 0, 0)
green = (47, 79, 79)
white = (255, 255, 255)

# экран
sc.fill(green)

# slider
osn = pygame.Surface((200, 30))
polz = pygame.Surface((10, 30))

polz.fill(gold)
osn.fill(white)

# переменные
v = 0  # скорость
x = 0  # координата ползунка
l = 0
c = 3000000000
b = v ** 2 / c ** 2
y = 1 / math.sqrt(1 - b)
osn.blit(polz, (x, 20))
sc.blit(osn, (500, 600))

# стержни
l_0 = 300  # натуральная длина
surf_l = pygame.Surface((l_0, 20))
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

r = (l_s / l_0) * 100
rit = font.render(str(r), 0, gold)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            x, l = pygame.mouse.get_pos()
            x = x - 505
            if x > 190:
                x = 190
                v = x * 15789473
            elif x < 0:
                x = 0
                v = x * 15789473
            else:
                v = x * 15789473

    # экран
    sc.fill(green)

    # надписи
    sc.blit(follow, (350, 0))
    sc.blit(nach_zn, (480, 600))
    sc.blit(con_zn, (705, 600))

    # текущее значение скорости
    tec_zn = font.render(str(v), 0, gold)
    place = tec_zn.get_rect(center=(600, 650))
    sc.blit(tec_zn, place)

    # гамма и бетта
    b = v ** 2 / c ** 2
    y = 1 / math.sqrt(1 - b)

    # меняю длину стержня
    l_s = round(l_0 / y, 3)
    surf_s = pygame.Surface((l_s, 20))
    surf_s.fill(gold)

    r = round((l_s / l_0) * 100, 2)
    rit = font.render(str(r) + '%', 0, gold)
    sc.blit(rit, (450, 500))

    # рисую стержни
    sc.blit(surf_l, (50, 200))
    sc.blit(surf_s, (50, 500))

    # рисую линию
    pygame.draw.line(sc, gold, [0, 360], [1200, 360], 4)

    osn.fill(white)

    osn.blit(polz, (x, 0))
    sc.blit(osn, (500, 600))

    pygame.display.update()
    pygame.time.delay(100)
