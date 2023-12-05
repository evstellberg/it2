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
        self.navnfont = pygame.font.SysFont('Corbel', 14)

        self.FPS = 30
        self.REFRESH = pygame.USEREVENT+1
        pygame.time.set_timer(self.REFRESH, 1000//self.FPS)    

        self.bg = pygame.image.load("ting og tang/store prosjekter/pokemon v4/grafikk/annen_grafikk/battlebackground.jpg")
        self.playerImage = pygame.image.load(player.image)
        self.enemyImage = pygame.image.load(enemy.image)

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
                self.lagre()
                self.save_game(self.savedData, "savedGame.pickle") #Kan legges til system for flere lagringsfiler senere
                self.game_state = "loading"
            elif self.musPåKnapp(85, 70) == True:
                self.savedData = self.load_game("savedGame.pickle")
                self.overskriv()
                self.game_state = "loading"
        if self.overlay == "bag":
            if self.musPåKnapp(185, 70) == True:
                actions.potion(player)
                self.overlay = ""
                self.fight_state = "enemy"
        if self.overlay == "seier":
            if self.musPåKnapp(-120, 70) == True:
                player.setXp(player.getXp() + 250)
                enemy.setCreature()
                enemy.setLvl(player.getLvl())
                self.overlay = ""

    def overskriv(self):
        player.setHp(self.savedData["spillerHp"])
        player.setMaxHp(self.savedData["spillerMaxHp"])
        player.setNavn(self.savedData["spillerNavn"])
        player.setLvl(self.savedData["spillerLvl"])
        player.setAtck(self.savedData["spillerAtck"])
        player.setDfnc(self.savedData["spillerDfnc"])
        player.setImg(self.savedData["spillerImg"])
        enemy.setHp(self.savedData["fiendeHp"])
        enemy.setMaxHp(self.savedData["fiendeMaxHp"])
        enemy.setNavn(self.savedData["fiendeNavn"])
        enemy.setLvl(self.savedData["fiendeLvl"])
        enemy.setAtck(self.savedData["fiendeAtck"])
        enemy.setDfnc(self.savedData["fiendeDfnc"])
        enemy.setImg(self.savedData["fiendeImg"])
        self.playerImage = pygame.image.load(player.image)
        self.enemyImage = pygame.image.load(enemy.image)


    def lagre(self):
        self.savedData["spillerHp"] = player.getHp()
        self.savedData["spillerMaxHp"] = player.getMaxHp()
        self.savedData["spillerNavn"] = player.getNavn()
        self.savedData["spillerLvl"] = player.getLvl()
        self.savedData["spillerAtck"] = player.getAtck()
        self.savedData["spillerDfnc"] = player.getDfnc()
        self.savedData["spillerImg"] = player.image
        self.savedData["fiendeHp"] = enemy.getHp()
        self.savedData["fiendeMaxHp"] = enemy.getMaxHp()
        self.savedData["fiendeNavn"] = enemy.getNavn()
        self.savedData["fiendeLvl"] = enemy.getLvl()
        self.savedData["fiendeAtck"] = enemy.getAtck()
        self.savedData["fiendeDfnc"] = enemy.getDfnc()
        self.savedData["fiendeImg"] = enemy.image


    def navnTekst(self, spiller, fiende):
        spillertext = self.navnfont.render(spiller, True, (0,0,0))
        self.screen.blit(spillertext, (self.width/2-spillertext.get_rect()[2]/2 -350,self.height/2+130))
        fiendetext = self.navnfont.render(fiende, True, (200,200,200))
        self.screen.blit(fiendetext, (self.width/2-fiendetext.get_rect()[2]/2 + 350,self.height/2-270))

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
                self.navnTekst(player.getNavn(), enemy.getNavn())

                self.screen.blit(self.playerImage, (100, 325))
                self.screen.blit(self.enemyImage, (575, 225))
                
                self.mouse = pygame.mouse.get_pos()
                
                #KAMP-MENY
                if self.fight_state == "meny":
                    if player.isFainted() == True:
                        self.overlay = "tap"
                    
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
                                actions.tackle(enemy, player)
                                self.fight_state = "enemy"
                            if self.musPåKnapp(-245, 350) == True:
                                actions.hardTackle(enemy, player)
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
                    if enemy.isFainted() == True:
                        self.fight_state = "meny"
                        self.overlay = "seier"
                    
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
                        actions.tackle(player, enemy)

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

                if self.overlay == "seier":
                    self.gjennomsiktig(self.screen, (0, 0, 0, 200), (0, 0, 800, 600))
                    self.dimm()
                    self.tekst(195, "VICTORY!")
                    self.tekst(0, f"You are now {player.getLvl()} Lvl")
                    self.knapp(-120, 70, "CONTINUE")

                if self.overlay == "tap":
                    self.gjennomsiktig(self.screen, (0, 0, 0, 200), (0, 0, 800, 600))
                    self.dimm()
                    self.tekst(195, "LOSS")
                    self.knapp(-120, 70, "RESTART")


            pygame.display.update() 

#creaturegenerator
class creatureGeneratorClass:
    def __init__(self):
        self.hp = [0, 10, 20]
        self.navn = ["Jo Bjørnar", "Katt", "Vildkatten"]
        self.image = ["ting og tang/store prosjekter/pokemon v4/grafikk/creatures/joBjornar.jpg", "ting og tang/store prosjekter/pokemon v4/grafikk/creatures/katt.jpg", "ting og tang/store prosjekter/pokemon v4/grafikk/creatures/vildkatten.jpeg"]
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
    def __init__(self):
        self.hp = 100
        self.maxHp = 100
        self.navn = "e"
        self.lvl = 1
        self.atck = 20
        self.dfnc = 0
        self.image = "e"

    def getHp(self):
        return self.hp + 10*self.getLvl()
    
    def getMaxHp(self):
        return self.maxHp + 10*self.getLvl()

    def getNavn(self):
        return self.navn
    
    def getLvl(self):
        return self.lvl
    
    def getAtck(self):
        return self.atck + 9*self.getLvl()
    
    def getDfnc(self):
        return self.dfnc + 0.01*self.getLvl()
        
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

    def setImg(self, updatedImg):
        self.image = updatedImg

    def setCreature(self):
        creatureStats = generator.getCreature()
        self.setMaxHp(creatureStats[0])
        self.setHp(creatureStats[0])
        self.setNavn(creatureStats[1])
        self.setAtck(creatureStats[2])
        self.setDfnc(creatureStats[3])
        self.setImg(generator.image[generator.navn.index(self.getNavn())])


    def isFainted(self):
        if self.hp <= 0:
            return True

class playerCreature(creature):
    def __init__(self):
        super().__init__()
        self.xp = 0

    def getXp(self):
        return self.xp
    
    def setXp(self, updatedXp):
        self.xp = updatedXp
        self.levelUp()

    def levelUp(self):
        while self.getXp() >= 100:
            self.setXp(self.getXp() - 100 * (1 + (0.1*self.getLvl())))
            self.setLvl(self.getLvl() + 1)
            print(self.getLvl())
        



#moveset
class creatureActions:
    def __init__(self):
        pass

    #Moves

    def tackle(self, enemy, player):
        enemy.setHp(enemy.getHp() - player.getAtck())
        

    def hardTackle(self, enemy, player):
        enemy.setHp(enemy.getHp() - player.getAtck()*1.5)
        
    
    def potion(self, player):
        player.setHp(player.getHp() + 60)
        

    

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
player = playerCreature()
playerHealthbar = healthbar()
enemy = creature()
enemyHealthbar = healthbar()
generator = creatureGeneratorClass()
actions = creatureActions()

#set creaturestats
player.setCreature()
enemy.setCreature()

#mainGameLoop
mainGame().mainLoop() 