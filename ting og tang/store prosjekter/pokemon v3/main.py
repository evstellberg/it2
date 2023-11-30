#bibliotek
import random
import pygame
#klasser

#creaturegenerator
class creatureGeneratorClass:

    def __init__(self):
        self.hp = [0, 10, 20]
        self.navn = ["monster1", "monster2", "monster3"]
        self.atck = [5, 10, 15]
        self.dfnc = [1, 2, 3]

    def generateHp(self):
        return random.choice(self.hp)
    
    def generateName(self):
        return random.choice(self.navn)

    def generateAtck(self):
        return random.choice(self.atck)
    
    def generateDfnc(self):
        return random.choice(self.dfnc)
    
    def getCreature(self):
        creatureStats = [self.generateHp() + 100, self.generateName(), self.generateAtck() + 20, self.generateDfnc()]
        return creatureStats
    
#Datalagring
class creature:
    def __init__(self, number):
        self.hp = 100
        self.navn = ""
        self.lvl = 1
        self.atck = 20
        self.dfnc = 0

    def getHp(self):
        return self.hp
    
    def getNavn(self):
        return self.navn
    
    def getLvl(self):
        return self.lvl
    
    def getAtck(self):
        return self.atck
    
    def getDfnc(self):
        return self.dfnc
        
    def setHp(self, updatedHp):
        self.hp = updatedHp
    
    def setNavn(self, updatedNavn):
        self.navn = updatedNavn

    def setLvl(self, updatedLvl):
        self.lvl = updatedLvl

    def setAtck(self, updatedAtck):
        self.atck = updatedAtck

    def setDfnc(self, updatedDfnc):
        self.dfnc = updatedDfnc

    def setCreature(self):
        creatureStats = generator.getCreature()
        print(creatureStats)
        self.hp = creatureStats[0]
        self.navn = creatureStats[1]
        self.atck = creatureStats[2]
        self.dfnc = creatureStats[3]

    def fainted(self):
        if self.hp <= 0:
            return True

#moveset
class playerCreatureActions:
    def __init__(self):
        pass

    #Moves

    def tackle(self):
        enemy.hp = enemy.hp - player.atck
        print(enemy.hp)

#objekter
player = creature(1)
enemy = creature(2)
generator = creatureGeneratorClass()
playerActions = playerCreatureActions()



#pygame-setup
pygame.init() 
game_state = "meny"
res = (800,600) 
screen = pygame.display.set_mode(res) 
  

color = (255,255,255) 

color_light = (170,170,170) 
  
color_dark = (100,100,100) 

width = 800

height = 600
  
smallfont = pygame.font.SysFont('Corbel',35) 

#funksjoner
def onStart():
    player.setCreature()
    enemy.setCreature()

def knapp(hoyde, bredde, innhold):
    if width/2-bredde <= mouse[0] <= width/2-bredde + 140 and height/2-hoyde <= mouse[1] <= height/2-hoyde + 40: 
        pygame.draw.rect(screen,color_light,[width/2 - bredde,height/2 - hoyde,140,40]) 
            
    else: 
        pygame.draw.rect(screen,color_dark,[width/2 - bredde,height/2 - hoyde,140,40])
    text = smallfont.render(innhold, True, color)
    screen.blit(text, (width/2-text.get_rect()[2]/2,height/2-(hoyde-5)))

def tekst(hoyde, innhold):
    text = smallfont.render(innhold, True, color)
    screen.blit(text, (width/2-text.get_rect()[2]/2,height/2-hoyde))

def musPåKnapp(hoyde, bredde):
    if width/2-bredde <= mouse[0] <= width/2-bredde+140 and height/2-hoyde <= mouse[1] <= height/2-hoyde+40:
        return True
    else:
        return False

#Vanlig kode

onStart()


while True: #main-game-loop
    if game_state == "meny": #startmeny
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 

            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if musPåKnapp(20,70) == True:
                    game_state = "instillinger"
                elif musPåKnapp(100, 70) == True:
                    game_state = "spill"
                elif musPåKnapp(-60, 70) == True:
                    pygame.quit()
                    
        screen.fill((60,25,60)) 
        
        mouse = pygame.mouse.get_pos() 
        
        knapp(20, 70, "OPTIONS")
        knapp(100, 70, "START")
        knapp(-60, 70, "QUIT")
        
    elif game_state == "instillinger":
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 

            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if musPåKnapp(-60, 70):
                    game_state = "meny"

        screen.fill((60,25,60)) 
        
        mouse = pygame.mouse.get_pos()

        knapp(-60, 70, "BACK")

        tekst(95, "W.I.P")
    
   # elif game_state == "spill":

    pygame.display.update() 