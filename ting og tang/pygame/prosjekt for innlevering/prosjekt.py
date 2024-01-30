import pygame as pg
import keyboard
#import random

visible = True


class game(object):
    
    def __init__(self):
        pg.init()
        self.res = (600, 900)
        self.screen = pg.display.set_mode(self.res)
        self.FPS = 60
        self.clock = pg.time.Clock()
        self.visible = True

        self.bg = pg.image.load("ting og tang/store prosjekter/pokemon v4/grafikk/annen_grafikk/battlebackground.jpg")

    def loop(self):
        while True:
            for ev in pg.event.get(): 
                if ev.type == pg.QUIT: 
                    pg.quit()
                if ev.type == pg.MOUSEBUTTONDOWN:
                    x = (300 - mouse[0])
                    print(x)
                    y = (mouse[1] - 130)
                    print(y)
                    for i in range(10):
                        balls[i].x_speed = x/y
                    self.visibleSwitch()
                    #self.visible = False
                                 
                    
                    print(mouse[1])
            
            self.screen.fill((10,10,10))

            mouse = pg.mouse.get_pos()

            for i in range(10):
                if self.visible == True:
                    balls[i].draw()
                    balls[i].move()
                    balls[i].gravity()
                balls[i].anyBouncesLeft()

            pg.display.update()
            self.clock.tick(self.FPS)
    
    def visibleSwitch(self):
        if self.visible == True:
            self.visible = False
        elif self.visible == False:
            self.visible = True
        print(self.visible)

class Ball():
    def __init__(self, x, y, x_speed, y_speed, rad, window, bouncelimit):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rad = rad
        self.window = window
        self.bounces = 0
        self.bouncelimit = bouncelimit
    
    def draw(self):
        colour = self.decideColour()
        #print(colour)
        pg.draw.circle(self.window, (colour), (self.x, self.y), self.rad)
    
    def move(self):
        if ((self.x - self.rad) <= 0) or ((self.x + self.rad) >= self.window.get_width()):
            self.x_speed = -self.x_speed
            self.bounces += 1
        if ((self.y - self.rad) <= 0) or ((self.y + self.rad) >= self.window.get_height()):
            self.bounces += 1
            self.y_speed = -(self.y_speed * 0.9)
            self.y += -10
            #print(self.y_speed)
        
        self.y += self.y_speed
        self.x += self.x_speed
    
    def gravity(self):
        if self.bounces > 1:
            self.y_speed += 0.2

    def anyBouncesLeft(self):
        if self.bounces >= self.bouncelimit:
            self.visibleSwitch()

    # def visibleSwitch(self):
    #     global visible
    #     if visible == True:
    #         visible = False
    #     if visible == False:
    #         visible = True
        
    def decideColour(self):
        if self.bounces < 15:
            return(51, 255, 51)
        elif self.bounces < 25:
            return(255, 255, 0)
        else:
            return(204, 0, 0)

#ball = Ball(10, 450, 10, 2, 5, game().screen, 20)
        
balls = [Ball(300+i*10, 15+i*10, 10, 2, 5, game().screen, 30) for i in range(10)]


game().loop()