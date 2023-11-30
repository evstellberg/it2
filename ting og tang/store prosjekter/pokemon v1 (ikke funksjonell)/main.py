#relaterte klasser og/eller pythonbibliotek
from creatureData import creature
from creatureGenerator import creatureGeneratorClass
from creatureActions import playerCreatureActions

#objekter
player = creature(1)
enemy = creature(2)
generator = creatureGeneratorClass()
playerActions = playerCreatureActions()

#funksjoner
def onStart():
    player.setCreature()
    enemy.setCreature()

#Vanlig kode
while True: #startloop
    print('"pokemon"\nStart [WRITE start] + [ENTER]\nSettings [WRITE settings] + [ENTER]')
    svar = input()
    if svar == "settings":
        print("W.I.P")
        svar = input()
    elif svar == "start":
        break

onStart()
playerActions.tackle()
#while True: #fremtidig main-game-loop