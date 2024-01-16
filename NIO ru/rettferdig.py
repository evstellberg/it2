NM = input()
NMSplit = NM.split(" ")

N = int(NMSplit[0])
M = int(NMSplit[1])

#print(N)
#print(M)

tallrekke = []

Arne = 0
Berit = 0
runde = 1

sjekk = True
x = 0
y = 0

for i in range(0,N):
    tallrekke.append(int(input()))

def optimaltTall():
    x = 0
    y = 0
    sjekk = True
    
    if len(tallrekke) == 1:
        sjekk = False
        return [tallrekke[0], y, x]

    # if tallrekke[x] > tallrekke[x+1]:
    #     return([tallrekke[x], tallrekke[x+1]])
    # else:
    #     sjekk = True
    
    while sjekk == True:
        if tallrekke[x] + y > tallrekke[x+1]:
            sjekk = False
            return([tallrekke[x], y, x])
        else:
            y += tallrekke[x+1]
            x += 1
        
for i in range(0,N):
    
    if tallrekke:
        #print(optimaltTall())
        result = optimaltTall()
            
        for i in range(1,result[2]+1):
            tallrekke.pop(0)
        print(tallrekke)

        if runde == 1:
            Arne += result[0]
            Berit += result[1]
            runde = 2
        else:
            Arne += result[1]
            Berit += result[0]
            runde = 1
    
print([Arne, Berit])




#print(tallrekke)