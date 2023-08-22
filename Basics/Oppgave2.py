'''Oppgave 2: Lag et program som ber brukeren om å skrive inn et tall mellom 1 og 10, og så sjekker om tallet er likt, større eller mindre enn et tilfeldig valgt tall. Programmet skal skrive ut om brukeren gjettet riktig, for  høyt eller for lavt, og hva det tilfeldige tallet var. For å velge et tilfeldig tall, kan du bruke funksjonen random.randint(a, b) fra modulen random, som gir et heltall mellom a og b (inkludert). For eksempel, hvis brukeren skriver inn “5” og det tilfeldige tallet er “7”, skal programmet skrive ut “Du gjettet for lavt. Det tilfeldige tallet var 7.”'''

import random

sjekk = 0
x = 0

tilfeldigTall = random.randint(1,10)

while (sjekk < 1):
    x += 1
    brukerTall = int(input("Tipp et tilfeldig tall fra 1 til 10: "))
    if brukerTall < tilfeldigTall:
        print("Tallet ditt er lavere enn det tilfeldige tallet.")
    elif brukerTall > tilfeldigTall:
        print("Tallet ditt er høyere enn det tilfeldige tallet.")
    else:
        print("Du tippet tallet! Du brukte " + str(x) + " forsøk")
        sjekk = 1
