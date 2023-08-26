import pygame as pg
import keyboard

pg.init()

VINDU_BREDDE = 220
VINDU_HOYDE = 160
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

font = pg.font.SysFont("Arial", 24)

fortsett = True
steg = 0

class Strek:
    def __init__(self, x, y, fart, vindusobjekt, fargeA, fargeB, fargeC, bredde, hoyde):
        self.x = x
        self.y = y
        self.fart = fart
        self.vindusobjekt = vindusobjekt
        self.fargeA = fargeA
        self.fargeB = fargeB
        self.fargeC = fargeC
        self.bredde = bredde
        self.hoyde = hoyde
    def tegn(self):
        pg.draw.rect(self.vindusobjekt, (self.fargeA, self.fargeB, self.fargeC), (self.x, self.y, self.bredde, self.hoyde))

    def flytt(self):
        if self.x == 0:
            if ((self.y) <= 0) or ((self.y + self.hoyde) >= self.vindusobjekt.get_height()):
                self.fart = -self.fart

            self.y += self.fart
        else:
            if ((self.x) <= 0) or ((self.x + self.bredde) >= self.vindusobjekt.get_width()):
                self.fart = -self.fart

            self.x += self.fart

strekVertHvit = Strek(60, 0, 0.01, vindu, 255, 255, 255, 40, 160)
strekVertBlo = Strek(70, 0, 0.01, vindu, 0, 32, 91, 20, 160)
strekHorHvit = Strek(0, 60, 0.01, vindu, 255, 255, 255, 220, 40)
strekHorBlo = Strek(0, 70, 0.01, vindu, 0, 32, 91, 220, 20)

while fortsett:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    vindu.fill((186, 12, 47))

    """strekVertHvit.tegn()
    strekVertHvit.flytt()
    strekVertBlo.tegn()
    strekVertBlo.flytt()
    strekHorHvit.tegn()
    strekHorHvit.flytt()
    strekHorBlo.tegn()
    strekHorBlo.flytt()"""
    
    """def on_press(key):
        print("hei")"""
    
    if steg == 0:
        strekVertHvit.tegn()
        strekVertHvit.flytt()
        
        strekVertHvitx = strekVertHvit.x
    if steg == 1:
        pg.draw.rect(vindu, (255, 255, 255), (strekVertHvitx, 0, 40, 160))

        strekVertBlo.tegn()
        strekVertBlo.flytt()

        strekVertBlox = strekVertBlo.x
    if steg == 2:
        pg.draw.rect(vindu, (255, 255, 255), (strekVertHvitx, 0, 40, 160))
        pg.draw.rect(vindu, (0, 32, 91), (strekVertBlox, 0, 20, 160))
        
        strekHorHvit.tegn()
        strekHorHvit.flytt()

        strekHorHvity = strekHorHvit.y
    if steg == 3:
        pg.draw.rect(vindu, (255, 255, 255), (strekVertHvitx, 0, 40, 160))
        pg.draw.rect(vindu, (255, 255, 255), (0, strekHorHvity, 220, 40))
        pg.draw.rect(vindu, (0, 32, 91), (strekVertBlox, 0, 20, 160))
        
        
        strekHorBlo.tegn()
        strekHorBlo.flytt()

        strekHorBloy = strekHorBlo.y

    
    if steg == 4:
        poeng = abs(60 - strekVertHvitx) + abs(70 - strekVertBlox) + abs(60 - strekHorHvity) + abs(70 - strekHorBloy)
        print(f"Du var {poeng} piksler fra et perfekt flagg!")

    if keyboard.is_pressed("Space"):
        steg += 1
        keyboard.wait("a")

    #print(strekVertHvit.x)

    #pg.draw.rect(vindu, (255, 255, 255), (60, 0, 40, 160))
    #pg.draw.rect(vindu, (255, 255, 255), (0, 60, 220, 40))
    #pg.draw.rect(vindu, (0, 32, 91), (70, 0, 20, 160))
    #pg.draw.rect(vindu, (0, 32, 91), (0, 70, 220, 20))
    pg.display.flip()