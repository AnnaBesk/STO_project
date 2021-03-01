import pygame
import math

pygame.init()

# start
size = (1200, 700)
sc = pygame.display.set_mode(size)
pygame.display.set_caption('Маятник')

# colors
black = (0, 0, 0)
white = (255, 255, 255)
orange = (217, 108, 0)
red = (255, 0, 0)
lime = (37, 230, 11)

# screen
sc.fill(orange)

# font
font = pygame.font.SysFont('timesnewroman', 40)

# titles
follow = font.render('Welcome to ticker', 1, white)
sc.blit(follow, (450, 20))

# buttons
pygame.draw.rect(sc, lime, (130, 120, 140, 40))
b_start = font.render('START', 1, white)
b_start_pos = b_start.get_rect(center=(200, 140))
sc.blit(b_start, b_start_pos)
b_stop = font.render('STOP', 1, white)
b_stop_pos = b_stop.get_rect(center=(200, 140))

# timer
time_x = pygame.time.get_ticks()
start = False
count = 0
timer = pygame.Surface((200, 40))
timer.fill(black)
milliseconds = 0
seconds = 0
minutes = 0
smin = '00'
smil = '00'
ssec = '00'
time = font.render(str(minutes) + ':' + str(seconds) + ':' + str(milliseconds), 1, white)
place_t = time.get_rect(center=(100, 20))
timer.blit(time, place_t)
sc.blit(timer, (100, 70))

# ticker
angle = 65
angle_r = math.radians(65)
g = 9.8
r = 300
a = g * math.sin(math.radians(90 - angle))
del_angle = a / r
v = 0
sch = 0

pos_start_x = 600
pos_start_y = 150
pos_start = (pos_start_x, pos_start_y)

pos_x = math.cos(angle_r) * r
pos_y = math.sin(angle_r) * r
pos = (pos_x + pos_start_x, pos_y + pos_start_y)

pygame.draw.circle(sc, black, pos_start, 10, 10)
pygame.draw.line(sc, black, pos_start, pos, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if (130 < mouse[0] < 270) and (120 < mouse[1] < 160):
                start = True
                count += 1
                if count % 2 == 0:
                    start = False
                start_time = pygame.time.get_ticks()
    if start:
        # time
        minutes = (time_x - start_time) // 60000
        seconds = ((time_x - start_time) % 60000) // 1000
        milliseconds = ((time_x - start_time) % 60000) % 100
        smin = str(minutes)
        ssec = str(seconds)
        smil = str(milliseconds)
        if minutes < 10:
            smin = '0' + smin
        if seconds < 10:
            ssec = '0' + ssec
        if milliseconds < 10:
            smil = '0' + smil
        sc.fill(orange)
        pygame.draw.rect(sc, red, (130, 120, 140, 40))
        sc.blit(b_stop, b_stop_pos)

        # маятник
        a = g * math.sin(math.radians(90-angle))  # меняю ускорение
        del_angle = a / r  # меняю угловое ускорение
        d_a=math.degrees(del_angle)
        if v <= 0:
            r_1 = True
            sch += 1
        elif (sch % 2 == 1) and round(a)==0:
            r_1 = False
            del_angle = math.radians(3)
            a = 10
        elif (sch % 2 == 0) and round(a)==0:
            r_1 = False
            del_angle=math.radians(3)
            a=10
        if r_1:
            v = v + a
            if sch % 2 == 1:
                angle_r += del_angle
                angle+=d_a
            else:
                angle_r -= del_angle
                angle-=d_a
        if not r_1:
            v = v - a
            if sch % 2 == 1:
                angle_r += del_angle
                angle+=d_a
            else:
                angle_r -= del_angle
                angle-=d_a

        pos_x = math.cos(angle_r) * r
        pos_y = math.sin(angle_r) * r
        pos = (pos_x + pos_start_x, pos_y + pos_start_y)

        pygame.draw.circle(sc, black, pos_start, 10, 10)
        pygame.draw.line(sc, black, pos_start, pos, 3)
        print(a)
    if not start:
        pygame.draw.rect(sc, lime, (130, 120, 140, 40))
        b_start = font.render('START', 1, white)
        b_start_pos = b_start.get_rect(center=(200, 140))
        sc.blit(b_start, b_start_pos)

    time_x = pygame.time.get_ticks()
    timer.fill(black)
    time = font.render(smin + ':' + ssec + ':' + smil, 1, white)
    place_t = time.get_rect(center=(100, 20))
    timer.blit(time, place_t)
    sc.blit(timer, (100, 70))
    pygame.display.update()
    pygame.time.delay(10)
