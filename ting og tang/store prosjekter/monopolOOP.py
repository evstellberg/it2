import random
tiles = 27
loop = True
eiendommer = [
    #start
    {"navn": "Parkveien", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 0, "eier": "ingen"},
    #Prøv Lykken
    {"navn": "Kirkeveien", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 1, "eier": "ingen"},
    #Inntektsskatt
    {"navn": "Oslo S.", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 2, "eier": "ingen"},
    {"navn": "Kongens Gate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    #Sjanse
    {"navn": "Prinsens Gate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Øvre Slottsgate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    #Fengsel
    {"navn": "Nedre Slottsgate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Oslo Lysverker", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Trondheimsveien", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Nobels Gate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Skjøyen stasjon", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Grensen", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    #Prøv Lykken
    {"navn": "Gabels Gate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Ringgata", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    #Gratis Parkering
    {"navn": "Bygdøy Allé", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    #Sjanse
    {"navn": "Skarpsno", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Slemdal", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Grorud stasjon", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Karl Johans gate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Stortorget", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Vannverket", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Torggata", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    #Gå i fengsel
    {"navn": "Trosterudveien", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Pilestredet", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    #Prøv Lykken
    {"navn": "Sinsen", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    {"navn": "Bryn stasjon", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    #Sjanse
    {"navn": "Ullevål Hageby", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    #Luksusskatt
    {"navn": "Rådhusplassen", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
]

spiller1Eiendom = []
spiller2Eiendom = []

class Spiller:
    def __init__(self, nummer, penger, posisjon):
        self.nummer = nummer
        self.penger = penger
        self.posisjon = posisjon
    
    eiendom = []

    def terningkasting(self):
        terningkast = random.randint(1,6)
        self.posisjon += terningkast
        if self.posisjon > tiles:
            self.posisjon = self.posisjon - tiles
        plass = eiendommer[self.posisjon]
        print(f'Du har landet på {plass["navn"]}')  
        if plass["eier"] == "ingen":
            if self.penger > plass["pris"]:
                x = input(f'Vil du kjøpe eiendommen? Den koster {plass["pris"]} penger. Du har {self.penger} penger.\ny/n\n')
                if x == "y":
                    self.penger = self.penger - plass["pris"]
                    plass["eier"] = self.nummer
                    self.eiendom.append(plass["plassering"])
            elif self.penger < plass["pris"]:
                print("Du har ikke råd til denne eiendommen")
                input("heieheiei")
        #if plass["eier"] == "spiller2":
            #spiller2.penger += plass["grunnleie"]
            #spiller1.penger = spiller1.penger - plass["grunnleie"]
            #print("Du betalte leie til den andre spilleren!")
    def spillerRunde(self):
        loop = True
        while loop == True:
            x = input(f"Spiller {self.nummer} sin tur. \nHva vil du gjøre? \nSe eiendommer[1] \nGi opp[2] \nTrille terning[3]\n")
            if x == "1":
                print("Kommer snart!")
                y = input("Hva vil du gjøre? \nGå tilbake [1]")
            if x == "2":
                exit()
            if x == "3":
                loop = False
                self.terningkasting()

spiller1 = Spiller(1, 10000, -1)
spiller2 = Spiller(2, 10000, -1)

while True:
    spiller1.spillerRunde()
    spiller2.spillerRunde()