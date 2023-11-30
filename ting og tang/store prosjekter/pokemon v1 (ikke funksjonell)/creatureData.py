#relaterte klasser og/eller pythonbibliotek
from creatureGenerator import creatureGeneratorClass

#nye klasser
class creature:
    def __init__(self, enemy):
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

#objekter
generator = creatureGeneratorClass()

