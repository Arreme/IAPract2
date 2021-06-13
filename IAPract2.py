import random

#La lletra indica el "pal" de la carta i el numero [C -> cors, P -> piques, R -> Rombes)
c = ["C1","C2","C3","P1","P2","P3","R1","R2","R3"]
cAux = ["C1","C2","C3","P1","P2","P3","R1","R2","R3"]
solution =[["","",""],["","",""],["","",""]]
position = [0,0]
cC = ["C1","C2","C3"]
cP = ["P1","P2","P3"]
cR = ["R1","R2","R3"]


# Principal
def solve_card():
    print()
    print("Resolent...")

    printTable()
    # si no queden cartes a la baralla auxiliar
        # el problema esta resolt
    if len(cAux) == 0:
        print()
        print("Hem trobat solució: ")
        return True

    # agafar carta candidata
    # buscar lloc per la carta
        # mirar que sigui legal 
            # fiquem la carta on sigui legal
            # mirar si es solucio
                # si es completable es crida backtracking
                # sino es desfa i es torna a provar
    candidat = getRandCart()
    posicions_buides = find_all_empty()
    for position in posicions_buides:
        if (esLegal(candidat,position[0],position[1])):
            solution[position[0]][position[1]] = candidat
            if (solve_card()):
                return True
            solution[position[0]][position[1]] = ""
            cAux.append(candidat)



# Auxiliars 
def printTable():
    print( str(solution[0][:]).replace('[',"|").replace(']',"|").replace(','," |"),
           str(solution[1][:]).replace('[',"|").replace(']',"|").replace(','," |"),
           str(solution[2][:]).replace('[', "|").replace(']', "|").replace(',', " |"),
           sep ='\n')

def getRandCart():
    if len(cAux) != 1:
        var = random.randrange(0, cAux.__len__()-1)
    else:
        var = 0
    return cAux.pop(var)

def get_elements(row):
    total = 0
    # if (row < m.len() and row >= 0)
    for x in solution[row]:
        if (x != ""):
            total += 1
    return total

def compatible_pal(tipus,row):
    for elem in solution[row]:
        if elem in tipus:
            return False
    return True


def compatible_row(tipus, row):
    if (get_elements(row) <= get_elements(0) and get_elements(row) <= get_elements(1) and get_elements(row) <= get_elements(2)):
        return True
    return False

def find_all_empty():
    positions = []
    for row in range(3):
        for col in range(3):
            if (solution[row][col] == ""):
                positions.append([row,col])
    return positions

def esLegal(carta, fila, columna):
    retorn = False

    if (carta in cC): retorn = compatible_pal(cC, fila) and compatible_row(cC, fila) 
    elif (carta in cP): retorn = compatible_pal(cP, fila) and compatible_row(cP, fila) 
    elif (carta in cR): retorn = compatible_pal(cR, fila) and compatible_row(cR, fila) 

    return retorn

solution[0][0] = getRandCart()

""" 
condicions fila:
    -> NO dues cartes amb el mateix pal
    -> NO més d'1 carta en comparació a la resta de files
Sinó és possible avançar amb les condicions de la fila usant la carta actual, s'aplicarà backtracking 
"""
