tall = []

for i in range(1,101):
    tall.append(i)

lengde = len(tall)
if lengde == 100:
    print(f"Listen har rett mengde elementer, {lengde}")
else:
    print(f"Listen har feil mengde elementer, {lengde}")

def deling(liste, tall):
    print(f"Leter etter tall som er delelig med {tall}")
    resultat = []
    for i in range(0, len(liste)):
        if liste[i] % tall == 0:
            resultat.append(liste[i])
    return resultat

delteTall = (deling(tall, 7))

for i in range(0, len(delteTall)):
    print(delteTall[i])