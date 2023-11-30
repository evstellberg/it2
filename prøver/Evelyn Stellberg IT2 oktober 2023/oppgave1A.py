hoyde = (input("Hva er høyden til bildet?\n"))
bredde = int(input("Hva er bredden til bildet?\n"))

if hoyde.isnumeric() == True:
    hoyde = int(hoyde)
else:
    print("Dette er ikke et tall!")

if hoyde < bredde: 
    print("Landscape")
if bredde < hoyde:
    print("Portrait")
if bredde == hoyde:
    print("Ingen av delene, kvadrat")