#Programmet tar utgangspunkt i at ingen blir 100 år gammel

import datetime

dato = datetime.datetime.now()
ekteAar = dato.year - 2000
print(ekteAar)

foedselsnummer = input("Hva er fødselsnummeret ditt?\n")

def maanedTilTekst1():
    global maaned
    if maaned == "01":
        maaned = "januar"
    if maaned == "02":
        maaned = "februar"
    if maaned == "03":
        maaned = "mars"
    if maaned == "04":
        maaned = "april"
    if maaned == "05":
        maaned = "mai"
    if maaned == "06":
        maaned = "juni"
    if maaned == "07":
        maaned = "juli"
    if maaned == "08":
        maaned = "august"
    if maaned == "09":
        maaned = "september"
    if maaned == "10":
        maaned = "oktober"
    if maaned == "11":
        maaned = "november"
    if maaned == "12":
        maaned = "desember"

def maanedTilTekst2():
    global maaned
    maaneder = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"]
    if maaned[0] == 0:
        maaned = maaned[1]
    maaned = maaneder[int(maaned) - 1]

def aarFunksjon():
    global aar
    global ekteAar
    if int(aar) == ekteAar + 1:
        print("Ugyldig personnummer grunnet årstall")
        exit()
    if int(aar) < ekteAar and int(aar) > 0:
        aar = "20" + aar
    else:
        aar = "19" + aar

def kjonnFunksjon():
    tall = int(foedselsnummer[8])
    if tall % 2 == 0:
        return "kvinne"
    else:
        return "mann"


if len(foedselsnummer) != 11:
    exit()

if foedselsnummer[0] == "0":
    dag = foedselsnummer[1]
else:
    dag = foedselsnummer[0] + foedselsnummer[1]

maaned = foedselsnummer[2] + foedselsnummer[3]
aar = foedselsnummer[4] + foedselsnummer[5]





#maanedTilTekst1()
maanedTilTekst2()
aarFunksjon()

print(f"{dag}.{maaned}.{aar} ({kjonnFunksjon()})")

print(f"Fødselsdatoen er {dag}. {maaned} {aar} ({kjonnFunksjon()})")