import pygame as pg
import keyboard
import time
import random
from playsound import playsound

pg.init()

WINDOWWIDTH = 500
WINDOWHEIGHT = 500
window = pg.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])

font = pg.font.SysFont("Arial", 24)

fortsett = True

FPS = 60
fpsClock = pg.time.Clock()
ticks = 0

timing = [0,0,0,0,0,0,0]

def brikke(steg):
    if keyboard.is_pressed("Space"):
        timing[steg] = (60 + steg * 30) - ticks
        if timing[steg] < 2 and timing[steg] > -2:
            window.fill((255, 255, 255))


class gameObject:
    def __init__(self, x, y, speed, windowObject, red, green, blue, width, height):
        self.x = x
        self.y = y
        self.speed = speed
        self.windowObject = windowObject
        self.red = red
        self.blue = blue
        self.green = green
        self. width = width
        self.height = height
    def draw(self):
        pg.draw.rect(self.windowObject, (self.red, self.blue, self.green), (self.x, self.y, self.width, self.height))
    def move(self):
        self.x -= self.speed

test = gameObject(500, 237.5, 4.166, window, 0, 0, 255, 10, 25)
test2 = gameObject(500, 237.5, 4.166, window, 0, 0, 255, 10, 25)
test3 = gameObject(500, 237.5, 4.166, window, 0, 0, 255, 10, 25)
test4 = gameObject(500, 237.5, 4.166, window, 0, 0, 255, 10, 25)
test5 = gameObject(500, 237.5, 4.166, window, 0, 0, 255, 10, 25)
test6 = gameObject(500, 237.5, 4.166, window, 0, 0, 255, 10, 25)
test7 = gameObject(500, 237.5, 4.166, window, 0, 0, 255, 10, 25)


while fortsett:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    window.fill((30, 30, 30))

    gameObject(250, 235, 0, window, 255, 255, 255, 15, 30).draw()

    if ticks < 65:
        test.draw()
        test.move()
        brikke(0)
    if ticks > 30 and ticks < 95:
        test2.draw()
        test2.move()
        brikke(1)
    if ticks > 60 and ticks < 125:
        test3.draw()
        test3.move()
        brikke(2)
    if ticks > 90 and ticks < 155:
        test4.draw()
        test4.move()
        brikke(3)
    if ticks > 120 and ticks < 185:
        test5.draw()
        test5.move()
        brikke(4)
    if ticks > 150 and ticks < 215:
        test6.draw()
        test6.move()
        brikke(5)
    if ticks > 180 and ticks < 245:
        test7.draw()
        test7.move()
        brikke(6)
    if ticks > 245:
        print(timing[0] + timing[1] + timing[2] + timing[3] + timing[4] + timing[5] + timing[6])
        print(timing)
    pg.display.flip()
    fpsClock.tick_busy_loop(FPS)
    ticks += 1

