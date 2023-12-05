import random # bibliotek for tilfeldigheter
import pygame as pg
import keyboard

SETNINGER = ["det er kraftig goofy", "frfr ong fo sho", "moren din"]
print('Trykk "a" for å starte')
keyboard.wait("a")

poengsummer = [0, 0, 0] #antall feile bokstaver, feile ord og tid brukt (ms)

pg.init()

for i in range(10):
    setning = SETNINGER[random.randint(0, len(SETNINGER) - 1)]
    svar = input(setning)
    
    setningOrd = setning.split(" ")
    svarOrd = svar.split(" ")
    setningBokstaver = setning.split()
    svarBokstaver = svar.split()

    forskjellOrd = len(svarOrd) - len(setningOrd)
    if forskjellOrd < 0:
        for i in range(len(svarOrd)):
            if setningOrd[i] != svarOrd[i]:
                poengsummer[1] += 1
    

print(poengsummer)

        
    
