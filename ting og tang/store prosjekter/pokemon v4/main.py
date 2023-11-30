#bibliotek
import random
import pygame
import math
import sys
import time
import pickle
#klasser
class mainGame(object):

    def __init__(self):
        pygame.init() 
        self.game_state = "meny"
        self.fight_state = "meny"
        self.overlay = "" 
        self.continueFight = 0
        self.loading = 0
        self.res = (800,600) 
        self.screen = pygame.display.set_mode(self.res) 
        self.prikker = ""

        self.savedData = {"spillerHp": 1, "spillerMaxHp": 1, "spillerNavn": "hei", "spillerLvl": 1, "spillerAtck": 1, "spillerDfnc": 1,"fiendeHp": 1, "fiendeMaxHp": 1, "fiendeNavn": "", "fiendeLvl": 1, "fiendeAtck": 1, "fiendeDfnc": 1}


        self.color = (255,255,255) 
        self.color_light = (170,170,170) 
        self.color_dark = (100,100,100) 

        self.width = 800
        self.height = 600
        self.smallfont = pygame.font.SysFont('Corbel',35)
        self.navnfont = pygame.font.SysFont('Corbel', 12)

        self.FPS = 30
        self.REFRESH = pygame.USEREVENT+1
        pygame.time.set_timer(self.REFRESH, 1000//self.FPS)    

        self.bg = pygame.image.load("ting og tang/store prosjekter/pokemon v4/grafikk/annen_grafikk/battlebackground.jpg")

    def save_game(self, save_data, file_name):
        try:
            with open(file_name, 'wb') as file:
                pickle.dump(save_data, file)
                print("Game saved!")
        except IOError:
            print("Error while saving")

    def load_game(self, file_name):
        try:
            with open(file_name, 'rb') as file:
                save_data = pickle.load(file)
                print("Game loaded!")
                return save_data
        except (IOError, pickle.UnpicklingError):
            print("Error while loading")

    def knapp(self, hoyde, bredde, innhold):
        if self.width/2-bredde <= self.mouse[0] <= self.width/2-bredde + 140 and self.height/2-hoyde <= self.mouse[1] <= self.height/2-hoyde + 40: 
            pygame.draw.rect(self.screen,self.color_light,[self.width/2 - bredde,self.height/2 - hoyde,140,40]) 
            
        else: 
            pygame.draw.rect(self.screen,self.color_dark,[self.width/2 - bredde,self.height/2 - hoyde,140,40])
        text = self.smallfont.render(innhold, True, self.color)
        self.screen.blit(text, (self.width/2-bredde+70-text.get_rect()[2]/2,self.height/2-(hoyde-5)))

    def gjennomsiktig(self, skjerm, farge, firkant):
        shape_surf = pygame.Surface(pygame.Rect(firkant).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, farge, shape_surf.get_rect())
        skjerm.blit(shape_surf, firkant)

    def tekst(self, hoyde, innhold):
        text = self.smallfont.render(innhold, True, self.color)
        self.screen.blit(text, (self.width/2-text.get_rect()[2]/2,self.height/2-hoyde))

    def dimm(self):
        pygame.draw.rect(self.screen,(60,25,60),[self.width/2 - 250, self.height/2 - 225, 500, 450])

    def musPåKnapp(self, hoyde, bredde):
        if self.width/2-bredde <= self.mouse[0] <= self.width/2-bredde+140 and self.height/2-hoyde <= self.mouse[1] <= self.height/2-hoyde+40:
            return True
        else:
            return False
    
    def pauseButtons(self):
        if self.overlay == "pause":
            if self.musPåKnapp(185, 70) == True:
                print("eyyy")
                self.lagre()
                self.save_game(self.savedData, "savedGame.pickle") #Kan legges til system for flere lagringsfiler senere
                self.game_state = "loading"
            elif self.musPåKnapp(85, 70) == True:
                self.savedData = self.load_game("savedGame.pickle")
                self.overskriv()
                print(self.savedData)
                self.game_state = "loading"
        if self.overlay == "bag":
            if self.musPåKnapp(185, 70) == True:
                actions.playerPotion()
                self.overlay = ""
                self.fight_state = "enemy"

    def overskriv(self):
        player.setHp(self.savedData["spillerHp"])
        player.setMaxHp(self.savedData["spillerMaxHp"])
        player.setNavn(self.savedData["spillerNavn"])
        player.setLvl(self.savedData["spillerLvl"])
        player.setAtck(self.savedData["spillerAtck"])
        player.setDfnc(self.savedData["spillerDfnc"])
        enemy.setHp(self.savedData["fiendeHp"])
        enemy.setMaxHp(self.savedData["fiendeMaxHp"])
        enemy.setNavn(self.savedData["fiendeNavn"])
        enemy.setLvl(self.savedData["fiendeLvl"])
        enemy.setAtck(self.savedData["fiendeAtck"])
        enemy.setDfnc(self.savedData["fiendeDfnc"])

    def lagre(self):
        self.savedData["spillerHp"] = player.getHp()
        self.savedData["spillerMaxHp"] = player.getMaxHp()
        self.savedData["spillerNavn"] = player.getNavn()
        self.savedData["spillerLvl"] = player.getLvl()
        self.savedData["spillerAtck"] = player.getAtck()
        self.savedData["spillerDfnc"] = player.getDfnc()
        self.savedData["fiendeHp"] = player.getHp()
        self.savedData["fiendeMaxHp"] = player.getMaxHp()
        self.savedData["fiendeNavn"] = player.getNavn()
        self.savedData["fiendeLvl"] = player.getLvl()
        self.savedData["fiendeAtck"] = player.getAtck()
        self.savedData["fiendeDfnc"] = player.getDfnc()

    def navnTekst(self, spiller, fiende):
        spillertext = self.navnfont.render(spiller, True, self.color)
        self.screen.blit(spillertext, (self.width/2-spillertext.get_rect()[2]/2,self.height/2-0))
        fiendetext = self.navnfont.render(fiende, True, self.color)
        self.screen.blit(fiendetext, (self.width/2-fiendetext.get_rect()[2]/2,self.height/2-0))

    def mainLoop(self):
        while True:
            
            #MENY
            if self.game_state == "meny":
                for ev in pygame.event.get(): 
                        
                    if ev.type == pygame.QUIT: 
                        pygame.quit() 

                    if ev.type == pygame.MOUSEBUTTONDOWN: 
                        if self.musPåKnapp(20,70) == True:
                            self.game_state = "instillinger"
                        elif self.musPåKnapp(100, 70) == True:
                            self.game_state = "loading"
                            
                        elif self.musPåKnapp(-60, 70) == True:
                            pygame.quit()
                    
                                
                self.screen.fill((60,25,60)) 
                    
                self.mouse = pygame.mouse.get_pos() 
                    
                self.knapp(20, 70, "OPTIONS")
                self.knapp(100, 70, "START")
                self.knapp(-60, 70, "QUIT")

            #INSTILLINGER      
            elif self.game_state == "instillinger":
                for ev in pygame.event.get(): 
                        
                    if ev.type == pygame.QUIT: 
                        pygame.quit() 

                    if ev.type == pygame.MOUSEBUTTONDOWN: 
                        if self.musPåKnapp(-60, 70):
                            self.game_state = "meny"

                self.screen.fill((60,25,60)) 
                    
                self.mouse = pygame.mouse.get_pos()

                self.knapp(-60, 70, "BACK")

                self.tekst(95, "W.I.P")
                
            #LASTING
            elif self.game_state == "loading":
                for ev in pygame.event.get(): 
                        
                    if ev.type == pygame.QUIT: 
                        pygame.quit() 
                
                self.screen.fill((60, 25, 60))

                self.tekst(100, "LOADING")
                pygame.draw.rect(self.screen,(80,80,80),[200, 250, 400, 10])
                pygame.draw.rect(self.screen,(255,255,255),[200, 250, self.loading/2, 10])
                self.loading += 1
                if self.loading == 800:
                    self.loading = 0
                    self.game_state = "fight"
            
            #KAMP
            elif self.game_state == "fight":
                self.screen.fill((60,25,60))
                self.screen.blit(self.bg, (0, 0))
                pygame.draw.rect(self.screen,(255,0,0),[self.width/2 - 380, self.height/2 + 150, 300, 10])
                pygame.draw.rect(self.screen,(0,255,0),[self.width/2 - 380, self.height/2 + 150, playerHealthbar.getWidth(player.getMaxHp(), player.getHp())*3 + 1, 10])
                pygame.draw.rect(self.screen,(255,0,0),[self.width/2 + 80, self.height/2 - 250, 300, 10])
                pygame.draw.rect(self.screen,(0,255,0),[self.width/2 + 80, self.height/2 - 250, enemyHealthbar.getWidth(enemy.getMaxHp(), enemy.getHp())*3 + 1, 10])
                self.navnTekst("navn1", "navn2")
                
                self.mouse = pygame.mouse.get_pos()
                
                #KAMP-MENY
                if self.fight_state == "meny":
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT: 
                            pygame.quit() 
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            if self.musPåKnapp(-220, -220) == True:
                                pygame.quit()
                            if self.musPåKnapp(-220, 350) == True:
                                self.fight_state = "attack"
                            if self.musPåKnapp(-220, 70) == True:
                                self.overlay = "bag"

                            self.pauseButtons()

                        if ev.type == pygame.KEYDOWN:
                            if ev.key == pygame.K_ESCAPE:
                                if self.overlay != "":
                                    self.overlay = ""
                                else:
                                    self.overlay = "pause"
                        
                    self.knapp(-220, 350, "FIGHT")
                    self.knapp(-220, -220, "RUN")
                    self.knapp(-220, 70, "BAG")
                
                #KAMP-ANGREP
                elif self.fight_state == "attack":
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT: 
                            pygame.quit() 
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            if self.musPåKnapp(-220, -220) == True:
                                self.fight_state = "meny"
                            if self.musPåKnapp(-200, 350) == True:
                                actions.playerTackle()
                                self.fight_state = "enemy"
                            if self.musPåKnapp(-245, 350) == True:
                                actions.playerHardTackle()
                                self.fight_state = "enemy"

                            self.pauseButtons()

                        if ev.type == pygame.KEYDOWN:
                            if ev.key == pygame.K_ESCAPE:
                                if self.overlay != "":
                                    self.overlay = ""
                                else:
                                    self.overlay = "pause"
                    
                    self.knapp(-220, -220, "BACK")
                    self.knapp(-200, 350, "TACKLE")
                    self.knapp(-245, 350, "TACKLE +")

                #KAMP-FIENDE
                elif self.fight_state == "enemy":
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT: 
                            pygame.quit() 
                    if self.loading <= 60:
                        self.prikker = ""
                    elif self.loading > 60 and self.loading <= 120:
                        self.prikker = "."
                    elif self.loading > 120 and self.loading <= 180:
                        self.prikker = ".."
                    elif self.loading > 180 and self.loading <= 240:
                        self.prikker = "..." 
                    else:
                        self.loading = 0
                    
                    self.tekst(-220, f"ENEMY IS THINKING{self.prikker}")

                    self.loading += 1
                    self.continueFight += 1
                    if self.continueFight == 400:
                        self.continueFight = 0
                        self.loading = 0
                        actions.enemyTackle()
                        self.fight_state = "meny"
                if self.overlay == "bag":
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT: 
                            pygame.quit() 
                    self.gjennomsiktig(self.screen, (0, 0, 0, 200), (0, 0, 800, 600))
                    self.dimm()
                    self.knapp(185, 70, "POTION")

                if self.overlay == "pause":
                    self.gjennomsiktig(self.screen, (0, 0, 0, 200), (0, 0, 800, 600))
                    self.dimm()
                    self.knapp(185, 70, "SAVE")
                    self.knapp(85, 70, "LOAD")

            pygame.display.update() 

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
        self.maxHp = 100
        self.navn = ""
        self.lvl = 1
        self.atck = 20
        self.dfnc = 0

    def getHp(self):
        return self.hp
    
    def getMaxHp(self):
        return self.maxHp

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
        if self.hp > self.maxHp:
            self.hp = self.maxHp
    
    def setMaxHp(self, updatedMaxHp):
        self.maxHp = updatedMaxHp

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
        self.setMaxHp(creatureStats[0])
        self.setHp(creatureStats[0])
        self.setNavn(creatureStats[1])
        self.setAtck(creatureStats[2])
        self.setDfnc(creatureStats[3])

    def fainted(self):
        if self.hp <= 0:
            return True

#moveset
class creatureActions:
    def __init__(self):
        pass

    #Moves

    def playerTackle(self):
        enemy.setHp(enemy.getHp() - player.getAtck())
        print(enemy.hp)
    
    def enemyTackle(self):
        player.setHp(player.getHp() - enemy.getAtck())
        print(player.hp)

    def playerHardTackle(self):
        enemy.setHp(enemy.getHp() - player.getAtck()*1.5)
        print(enemy.hp)
    
    def enemyHardTackle(self):
        player.setHp(player.getHp() - enemy.getAtck()*1.5)
        print(player.hp)
    
    def playerPotion(self):
        player.setHp(player.getHp() + 60)
        print(player.hp)

    def enemyPotion(self):
        enemy.setHp(enemy.getHp() + 60)
        print(enemy.hp)

class healthbar:
    def __init__(self):
        self.bredde = 100
        self.hoyde = 5
        self.green = (255, 0, 0)
        self.red = (255, 0, 0)
    
    def calculateForhold(self, hp):
        return hp/100
    
    def getWidth(self, maxHp, currentHp):
        forhold = self.calculateForhold(maxHp)
        return currentHp / forhold


#objekter
player = creature(1)
playerHealthbar = healthbar()
enemy = creature(2)
enemyHealthbar = healthbar()
generator = creatureGeneratorClass()
actions = creatureActions()

#set creaturestats
player.setCreature()
enemy.setCreature()

#mainGameLoop
mainGame().mainLoop() 