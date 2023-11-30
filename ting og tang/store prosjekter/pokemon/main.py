#relaterte klasser og/eller pythonbibliotek
from creatureData import creature
from creatureGenerator import creatureGeneratorClass
from creatureActions import playerCreatureActions

#objekter
player = creature(1)
enemy = creature(2)
generator = creatureGeneratorClass()
playerActions = playerCreatureActions()

#globale variabler
startloop = True

#funksjoner
def onStart():
    player.setCreature()
    enemy.setCreature()

#Vanlig kode

#Koden under gjør ting 2 ganger for ingen grunn (spør Jo Bjørnar)

# while startloop == True: #startloop
#     print('"pokemon"\nStart [WRITE start] + [ENTER]\nSettings [WRITE settings] + [ENTER]')
#     svar = input()
#     if svar == "settings":
#         print("W.I.P")
#         svar = input()
#     elif svar == "start":
#         startloop = False

onStart()
playerActions.tackle()
#while True: #fremtidig main-game-loop