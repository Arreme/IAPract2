import random

#La lletra indica el "pal" de la carta i el numero [C -> cors, P -> piques, R -> Rombes)
c = ["C1","C2","C3","P1","P2","P3","R1","R2","R3"]
cAux = ["C1","C2","C3","P1","P2","P3","R1","R2","R3"]
m =[["  ","  ","  "],
    ["  ","  ","  "],
    ["  ","  ","  "]]

def printTable():
    print( str(m[0][:]).replace('[',"|").replace(']',"|").replace(','," |"),
           str(m[1][:]).replace('[',"|").replace(']',"|").replace(','," |"),
           str(m[2][:]).replace('[', "|").replace(']', "|").replace(',', " |"),
           sep ='\n')

def getRandCart():
    var = random.randrange(0, cAux.__len__()-1)
    return cAux.pop(var)

m[0][0] = getRandCart()
printTable()

