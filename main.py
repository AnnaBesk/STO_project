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

x_0 = 300  # натуральная длина
surf_l = pygame.Surface((x_0, 20))
surf_l.fill(gold)

x_s = 300  # длина, которую видим
surf_s = pygame.Surface((x_s, 20))
surf_s.fill(gold)

# шрифт
font = pygame.font.SysFont('timesnewroman', 32)

sc.fill(green)
follow = font.render('Специальная теория относительности', 1, gold)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    sc.blit(follow, (350, 0))
    sc.blit(surf_l, (50, 200))
    sc.blit(surf_s, (50, 500))
    pygame.draw.line(sc, gold, [0, 360], [1200, 360], 4)
    pygame.display.update()
