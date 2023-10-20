varer = [
{
"Vare-ID": "Asus Zenbook GH215",
"Varenavn": "Asus Laptop",
"Pris": 9999,
"Varelager": 10,
"Produktinfo": "En bærbar PC med 15.6 tommer skjerm, 8 GB RAM og 256 GB SSD",
"Tekniske egenskaper": {"prosessor": "Intel Core i5","grafikkort": "Intel Iris Xe Graphics","batterikapasitet": "Opptil 8 timer","vekt": "1.8 kg"},
"Farger": ["grå", "svart", "blå"]
},
{
"Vare-ID": "Samsung Galaxy S22 GH67",
"Varenavn": "Samsung mobiltelefon",
"Pris": 6999,
"Varelager": 20,
"Produktinfo": "En smarttelefon med 6.7 tommer skjerm, 128 GB lagring og 12 MP kamera",
"Tekniske egenskaper": {"prosessor": "Qualcomm Snapdragon 888","grafikkort": "Adreno 660","batterikapasitet": "4500 mAh","vekt": "200 g"},
"Farger": ["svart", "hvit", "grønn"]
},
{
"Vare-ID": "test", #Apple Airpods Pro Gen 3 (2023)
"Varenavn": "Trådløse hodetelefoner",
"Pris": 2499,
"Varelager": 30,
"Produktinfo": "Trådløse hodetelfoner med aktiv støydemping",
"Tekniske egenskaper": {"batterikapasitet": "Opptil 4.5 timer","vekt": "5.4 g"},
"Farger": ["gul", "hvit", "spygrønn"]
}
]

def infoUthenting(vareID):
    feil = True
    for i in range(0, len(varer)):
        if vareID == varer[i]["Vare-ID"]:
            print(f'Vare-ID: {varer[i]["Vare-ID"]}\nVarenavn: {varer[i]["Varenavn"]}\nPris: {varer[i]["Pris"]}\nVarelager: {varer[i]["Varelager"]}\nProduktinfo: {varer[i]["Produktinfo"]}\nTekniske egenskaper: {varer[i]["Tekniske egenskaper"]}\nFarger: {varer[i]["Farger"]}\n')   
            feil = False
    if feil == True:
        print("Det er ingen produkter med den Vare-IDen")

def prisEndring(vareID, pris):
    feil = True
    for i in range(0, len(varer)):
        if vareID == varer[i]["Vare-ID"]:
            varer[i]["Pris"] = pris
            feil = False
        infoUthenting(vareID)
    if feil == True:
        print("Det er ingen produkter med den Vare-IDen")

def fargeEndring(vareID, farge):
    feil = True
    for i in range(0, len(varer)):
        if vareID == varer[i]["Vare-ID"]:
            varer[i]["Farger"].append(farge)
            feil = False
        infoUthenting(vareID)
    if feil == True:
        print("Det er ingen produkter med den Vare-IDen")

def fargeFjerning(vareID, farge):
    feil = True
    for i in range(0, len(varer)):
        if vareID == varer[i]["Vare-ID"]:
            varer[i]["Farger"].remove(farge)
            feil = False
        infoUthenting(vareID)
    if feil == True:
        print("Det er ingen produkter med den Vare-IDen")

def egenskapEndring(vareID, nøkkel, egenskap):
    feil = True
    for i in range(0, len(varer)):
        if vareID == varer[i]["Vare-ID"]:
            varer[i]["Tekniske egenskaper"][nøkkel] = egenskap
            feil = False
        infoUthenting(vareID)
    if feil == True:
        print("Det er ingen produkter med den Vare-IDen")

print(f"Det er {len(varer)} produkter på lageret.")

for i in range(0, len(varer)):
    print(
        f'Vare-ID: {varer[i]["Vare-ID"]}\nVarenavn: {varer[i]["Varenavn"]}\nPris: {varer[i]["Pris"]}\nVarelager: {varer[i]["Varelager"]}\nProduktinfo: {varer[i]["Produktinfo"]}\nTekniske egenskaper: {varer[i]["Tekniske egenskaper"]}\nFarger: {varer[i]["Farger"]}\n'
    )

x = input("Hvilket produkt vil du vite mer om?")

infoUthenting(x)

y = input("Hva vil du endre prisen på?")
z = input("Hva er den nye prisen?")

prisEndring(y, z)

a = input("Hva vil du legge til en ny farge til?")
b = input("Hvilken farge?")

fargeEndring(a, b)

c = input("Hva vil du fjerne en farge fra?")
d = input("Hvilken farge?")

fargeFjerning(c, d)

e = input("Hvilket produkt vil du legge til en teknisk egenskap til?")
f= input("Hva er kategorien til egenskapen?")
g = input("Hva er egenskapen?")

egenskapEndring(e, f, g)