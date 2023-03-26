import pygame
from pygame.draw import *
from math import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((101, 67, 33))

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

# экран+окно
polygon(screen, (175, 238, 238), [(200, 25), (380, 25), (380, 165), (200, 165)])
polygon(screen, (135, 206, 235), [(210, 35), (280, 35), (280, 75), (210, 75)])
polygon(screen, (135, 206, 235), [(300, 35), (370, 35), (370, 75), (300, 75)])
polygon(screen, (135, 206, 235), [(300, 85), (370, 85), (370, 155), (300, 155)])
polygon(screen, (135, 206, 235), [(210, 85), (280, 85), (280, 155), (210, 155)])
polygon(screen, (140, 120, 50), [(0, 190), (400, 190), (400, 400), (0, 400)])

# передние лапы
draw_ellipse_angle(screen, (200, 115, 5), [46, 232, 71, 43], -70, 0)
draw_ellipse_angle(screen, (0, 0, 0), [46, 232, 71, 43], -70, 1)



# ноги и хвост
draw_ellipse_angle(screen, (200, 115, 5), [300, 233, 150, 40], -200, 0)
draw_ellipse_angle(screen, (0, 0, 0), [300, 233, 150, 40], -200, 1)



# кот
ellipse(screen, (200, 115, 5), (80, 200, 270, 85))
ellipse(screen, (0, 0, 0), (80, 200, 270, 85), 1)
ellipse(screen, (200, 115, 5), (40, 210, 120, 65))
ellipse(screen, (0, 0, 0), (40, 210, 120, 65), 1)


#уши
polygon(screen, (200, 115, 5),  [(45, 230), (40, 200), (70, 220)])
polygon(screen, (0, 0, 0), [(45, 230), (40, 200), (70, 220)], 1)
polygon(screen, (250, 180, 240),  [(48, 226), (43, 205), (65, 219)])
polygon(screen, (200, 115, 5),[(130, 220), (150, 200), (155, 230)])
polygon(screen, (0, 0, 0), [(130, 220), (150, 200), (155, 230)], 1)
polygon(screen, (250, 180, 240),  [(134, 218), (149, 205), (152, 226)])

#глаза
ellipse(screen, (114, 158, 47), (65, 230, 25, 17))
ellipse(screen, (114, 158, 47), (110, 230, 25, 17))
ellipse(screen, (0, 0, 0), (124, 230, 6, 15))
ellipse(screen, (0, 0, 0), (79, 230, 6, 15))
draw_ellipse_angle(screen, (255, 255, 255), [69, 233, 10, 3], -220, 0)
draw_ellipse_angle(screen, (255, 255, 255), [116, 233, 10, 3], -220, 0)



#ноги задние
ellipse(screen, (200, 115, 5), (250, 240, 100, 60))
ellipse(screen, (0, 0, 0), (250, 240, 100, 60), 1)

ellipse(screen, (200, 115, 5), (330, 278, 30, 50))
ellipse(screen, (0, 0, 0), (330, 278, 30, 50), 1)

ellipse(screen, (200, 115, 5), (110, 270, 80, 30))
ellipse(screen, (0, 0, 0),(110, 270, 80, 30), 1)


#нос и усы
polygon(screen, (255, 255, 255),  [(95, 250), (105, 250), (100, 255)])
polygon(screen, (0, 0, 0),  [(95, 250), (105, 250), (100, 255)], 1)
line(screen,(0, 0, 0), [100, 255], [100, 260], 1)
arc(screen,(0, 0, 0), (100, 258, 10, 4), pi,15 * pi / 8 )
arc(screen,(0, 0, 0), (90, 258, 10, 4), pi,15 * pi / 8 )



# усы
arc(screen, (0, 0, 0), [20, 250, 300, 200], 1.55, 1.9)
arc(screen, (0, 0, 0), [17, 254, 305, 205], 1.55, 1.9)
arc(screen, (0, 0, 0), [15, 258, 310, 210], 1.55, 1.9)

arc(screen, (0, 0, 0), [-80, 252, 305, 200], 1.55, 1.9)
arc(screen, (0, 0, 0), [-76, 256, 300, 200], 1.55, 1.9)
arc(screen, (0, 0, 0), [-72, 260, 300, 200], 1.55, 1.9)


# клубок и нитки
ellipse(screen, (128, 128, 128), (200, 310, 115, 80))
ellipse(screen, (0, 0, 0), (200, 310, 115, 80), 1)
arc(screen, (0, 0, 0), [200, 320, 100, 30], 0, pi / 2)
arc(screen, (0, 0, 0), [190, 340, 115, 47], 0, pi / 2)
arc(screen, (0, 0, 0), [243, 365, 118, 36], 2 * pi / 3, pi)
arc(screen, (0, 0, 0), [232, 345, 80, 80], 2 * pi / 3, pi)
arc(screen, (0, 0, 0), [225, 324, 118, 36], 2 * pi / 3, pi)

arc(screen, (128, 128, 128), (100 , 320, 300 , 60 ), pi, 3*pi / 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
