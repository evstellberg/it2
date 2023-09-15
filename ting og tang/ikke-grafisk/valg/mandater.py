partier = [{"partinavn": "Høyre", "stemmer": 38227, "mandater": 0}, {"partinavn": "Arbeiderpartiet", "stemmer": 26781, "mandater": 0}, {"partinavn": "Fremskrittspartiet", "stemmer": 15251, "mandater": 0}, {"partinavn": "Sosialistisk venstreparti", "stemmer": 14394, "mandater": 0}, {"partinavn": "Bergenslisten", "stemmer": 7363, "mandater": 0}, {"partinavn": "Venstre", "stemmer": 7202, "mandater": 0}, {"partinavn": "Miljøpartiet de grønne", "stemmer": 7124, "mandater": 0}, {"partinavn": "Industri- og næringspartiet", "stemmer": 5858, "mandater": 0}, {"partinavn": "Rødt", "stemmer": 5765, "mandater": 0}, {"partinavn": "Kristelig folkeparti", "stemmer": 4873, "mandater": 0}, {"partinavn": "Senterpartiet", "stemmer": 3374, "mandater": 0}, {"partinavn": "Pensjonistpartiet", "stemmer": 2517, "mandater": 0}]

for i in range(0, len(partier)):
        stemmer = partier[i]["stemmer"]
        stemmer = stemmer/1.4
        partier[i]["stemmer"] = stemmer



for i in range(1, 67):
    for j in range(0, len(partier)):
        stemmer = partier[j]["stemmer"]
        mandater = partier[j]["mandater"]
        stemmer = stemmer/((2*mandater)+1)
        print(stemmer)

def sammenligning():
    vinner = ""
    vinnerVerdi = 0
    for i in range(0, len(partier)):
        parti = partier[i]["partinavn"]
        partiVerdi = partier[i]
        
