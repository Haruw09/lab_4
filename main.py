import pygame
from pygame.draw import *
import random
import math

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


def fence(x, y, width, height):
    """

    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    rect(screen, peru, (x, y, width, height))
    for j in range(width // 20):
        rect(screen, black, (x + j * 20, y, 20, height), 1)




fence(0, 0, 300, 160)
fence(0, 60, 140, 140)
fence(170, 80, 130, 110)

# конура
polygon(screen, goldenrod, [(0, 140), (60, 150), (60, 220), (0, 210)])
polygon(screen, black, [(0, 140), (60, 150), (60, 220), (0, 210)], 1)
polygon(screen, goldenrod, [(60, 150), (120, 120), (120, 200), (60, 220)])
polygon(screen, black, [(60, 150), (120, 120), (120, 200), (60, 220)], 1)
polygon(screen, darkgoldenrod, [(0, 140), (30, 120), (60, 150)])
polygon(screen, black, [(0, 140), (30, 120), (60, 150)], 1)
polygon(screen, darkgoldenrod, [(30, 120), (90, 90), (120, 120), (60, 150)])
polygon(screen, black, [(30, 120), (90, 90), (120, 120), (60, 150)], 1)
polygon(screen, black, [(80, 160), (100, 150), (100, 206), (80, 213)])


def chain(x, y, size, length):
    X = x
    Y = y
    for i in range(length):
        fate = random.randint(0, 1)
        ellipse(screen, black, [X, Y, (3 - (-1) ** fate)*size * 3, (3 - (-1) ** (fate + 1))*size * 3], 2 * size)
        X = X + (2 - (-1) ** fate) * 2 * size
        Y = Y + (2 - (-1) ** (fate + 1)) * 2 * size


'''
Функция рисует цепь.
x, y - координаты первого звена
size - размер звена 
length - количество звеньев
'''


chain(80, 213, 1, 20)


def dog(x, y, size):
    ellipse(screen, sienna, [x, y, 10*math.sqrt(size**2), 30*math.sqrt(size**2)])
    ellipse(screen, sienna, [x + 5*size, y + 25*size, 15*math.sqrt(size**2), 10*math.sqrt(size**2)])
    ellipse(screen, sienna, [x + 60*size, y + 10*size, 10*math.sqrt(size**2), 30*math.sqrt(size**2)])
    ellipse(screen, sienna, [x + 65*size, y + 35*size, 15*math.sqrt(size**2), 10*math.sqrt(size**2)])
    ellipse(screen, sienna, [x + 40*size, y + 20*size, 10*math.sqrt(size**2), 30*math.sqrt(size**2)])
    ellipse(screen, sienna, [x + 45*size, y + 45*size, 15*math.sqrt(size**2), 10*math.sqrt(size**2)])
    ellipse(screen, sienna, [x - 20*size, y + 10*size, 10*math.sqrt(size**2), 30*math.sqrt(size**2)])
    ellipse(screen, sienna, [x - 15*size, y + 35*size, 15*math.sqrt(size**2), 10*math.sqrt(size**2)])
    ellipse(screen, sienna, [x - 15*size, y - 10*size, 80*math.sqrt(size**2), 40*math.sqrt(size**2)])
    rect(screen, sienna, (x + 45*size, y - 30*size, 30*math.sqrt(size**2), 30*math.sqrt(size**2)))
    ellipse(screen, saddlebrown, [x + 45*size, y - 30*size, 10*math.sqrt(size**2), 20*math.sqrt(size**2)])
    ellipse(screen, saddlebrown, [x + 70*size, y - 30*size, 10*math.sqrt(size**2), 20*math.sqrt(size**2)])
    ellipse(screen, white, [x + 50*size, y - 25*size, 7*math.sqrt(size**2), 5*math.sqrt(size**2)])
    ellipse(screen, white, [x + 65*size, y - 25*size, 7*math.sqrt(size**2), 5*math.sqrt(size**2)])
    circle(screen, black, (x + 53.5*size, y - 22*size), 2.5*math.sqrt(size**2))
    circle(screen, black, (x + 68.5*size, y - 22*size), 2.5*math.sqrt(size**2))
    rect(screen, black, (x + 55*size, y - 10*size, 10*math.sqrt(size**2), 2*math.sqrt(size**2)))
    polygon(screen, white, [(x + 55*size, y - 10*size), (x + 56*size, y - 12*size), (x + 57*size, y - 10*size)])
    polygon(screen, white, [(x + 63*size, y - 10*size), (x + 64*size, y - 12*size), (x + 65*size, y - 10*size)])


'''
Функция рисует собаку.
x, y - координаты правого уха собаки
size - размер
'''
dog(145, 160, 1)
dog(200, 230, 1.3)
dog(-80, 270, 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
