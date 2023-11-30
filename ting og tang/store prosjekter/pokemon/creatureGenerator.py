#relaterte klasser og/eller pythonbibliotek
import random

#nye klasser
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

