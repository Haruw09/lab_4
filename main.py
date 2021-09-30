import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((300, 300))

sienna = (160, 82, 45)
white = (255, 255, 255)
black = (0, 0, 0)
goldenrod = (218, 165, 32)
darkgoldenrod = (184, 134, 11)
peru = (205, 133, 63)
forestgreen = (34, 139, 34)
saddlebrown = (139, 69, 19)

screen.fill(forestgreen)
# забор1
rect(screen, peru, (0, 0, 300, 160))
for i in range(15):
    rect(screen, black, (i * 20, 0, 20, 160), 1)
# забор2
rect(screen, peru, (0, 60, 140, 140))
for i in range(7):
    rect(screen, black, (i * 20, 60, 20, 140), 1)
# забор3
rect(screen, peru, (170, 80, 130, 110))
for i in range(7):
    rect(screen, black, (170 + i * 20, 80, 20, 110), 1)
# конура
polygon(screen, goldenrod, [(0, 140), (60, 150), (60, 220), (0, 210)])
polygon(screen, black, [(0, 140), (60, 150), (60, 220), (0, 210)], 1)
polygon(screen, goldenrod, [(60, 150), (120, 120), (120, 200), (60, 220)])
polygon(screen, black, [(60, 150), (120, 120), (120, 200), (60, 220)], 1)
polygon(screen, darkgoldenrod, [(0, 140), (30, 120), (60, 150)])
polygon(screen, black, [(0, 140), (30, 120), (60, 150)], 1)
polygon(screen, darkgoldenrod, [(30, 120), (90, 90), (120, 120), (60, 150)])
polygon(screen, black, [(30, 120), (90, 90), (120, 120), (60, 150)], 1)
# цепь
polygon(screen, black, [(80, 160), (100, 150), (100, 206.6667), (80, 213.3333)])
ellipse(screen, black, [80, 213.3333, 10, 5], 2)
ellipse(screen, black, [85, 215, 5, 10], 2)
ellipse(screen, black, [85, 220, 10, 5], 2)
ellipse(screen, black, [90, 220, 10, 5], 2)
ellipse(screen, black, [95, 220, 10, 5], 2)
# собака 1 лапы
ellipse(screen, sienna, [145, 160, 10, 30])
ellipse(screen, sienna, [150, 185, 15, 10])
ellipse(screen, sienna, [205, 170, 10, 30])
ellipse(screen, sienna, [210, 195, 15, 10])
ellipse(screen, sienna, [185, 180, 10, 30])
ellipse(screen, sienna, [190, 205, 15, 10])
ellipse(screen, sienna, [125, 170, 10, 30])
ellipse(screen, sienna, [130, 195, 15, 10])
# собака 1 туловище
ellipse(screen, sienna, [130, 150, 80, 40])
# собака 1 голова
rect(screen, sienna, (190, 130, 30, 30))
ellipse(screen, saddlebrown, [185, 130, 10, 20])
ellipse(screen, saddlebrown, [215, 130, 10, 20])
ellipse(screen, white, [195, 135, 7, 5])
ellipse(screen, white, [210, 135, 7, 5])
circle(screen, black, (198.5, 138), 2.5)
circle(screen, black, (213.5, 138), 2.5)
rect(screen, black, (200, 150, 10, 2))
polygon(screen, white, [(200, 150), (201, 148), (202, 150)])
polygon(screen, white, [(208, 150), (209, 148), (210, 150)])
# собака 2 лапы
ellipse(screen, sienna, [205, 250, 10, 30])
ellipse(screen, sienna, [190, 275, 20, 10])
ellipse(screen, sienna, [225, 260, 10, 30])
ellipse(screen, sienna, [210, 285, 20, 10])
ellipse(screen, sienna, [285, 250, 10, 30])
ellipse(screen, sienna, [270, 275, 20, 10])
# собака 2 туловище
ellipse(screen, sienna, [210, 230, 80, 40])
# собака 2 голова
rect(screen, sienna, (200, 210, 30, 30))
ellipse(screen, saddlebrown, [195, 210, 10, 20])
ellipse(screen, saddlebrown, [225, 210, 10, 20])
ellipse(screen, white, [204, 215, 8, 5])
ellipse(screen, white, [219, 215, 8, 5])
circle(screen, black, (208, 218), 2.5)
circle(screen, black, (223, 218), 2.5)
rect(screen, black, (210, 230, 10, 2))
polygon(screen, white, [(210, 230), (211, 228), (212, 230)])
polygon(screen, white, [(218, 230), (219, 228), (220, 230)])
# собака 3 туловище
ellipse(screen, sienna, [-70, 270, 140, 60])
# собака 3 голова
rect(screen, sienna, (20, 230, 50, 50))
ellipse(screen, saddlebrown, [15, 230, 15, 30])
ellipse(screen, saddlebrown, [60, 230, 15, 30])
ellipse(screen, white, [30, 245, 10, 5])
ellipse(screen, white, [50, 245, 10, 5])
circle(screen, black, (35, 247), 3)
circle(screen, black, (55, 247), 3)
rect(screen, black, (35, 265, 20, 2))
polygon(screen, white, [(35, 265), (37, 261), (39, 265)])
polygon(screen, white, [(51, 265), (53, 261), (55, 265)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
