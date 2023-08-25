import pygame as pg

pg.init()

VINDU_BREDDE = 220
VINDU_HOYDE = 160
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

font = pg.font.SysFont("Arial", 24)

fortsett = True
while fortsett:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    vindu.fill((255, 255, 255))
    pg.draw.rect(vindu, (255, 0, 0), (0, 0, 220, 160))
    pg.draw.rect(vindu, (255, 255, 255), (60, 0, 40, 160))
    pg.draw.rect(vindu, (255, 255, 255), (0, 60, 220, 40))
    pg.draw.rect(vindu, (0, 0, 255), (70, 0, 20, 160))
    pg.draw.rect(vindu, (0, 0, 255), (0, 70, 220, 20))
    pg.display.flip()