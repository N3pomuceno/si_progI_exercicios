# Programa
"""
2
3
LEFT
RIGHT
SAME AS 2
5
LEFT
SAME AS 1
SAME AS 2
SAME AS 1
SAME AS 4
"""
#Subprogramas
def novaPosicao(p, com, hist):
    np = p
    if com == "LEFT":
        np += -1
        return np
    elif com == "RIGHT":
        np += 1
        return np
    else:
        p1, p2, num = com.split()
        del p1, p2
        num = int(num)
        com = hist[num-1]
        np = novaPosicao(p, com, hist)
        return np


#Principal
numDeCasos = int(input())
for ind in range(numDeCasos):
    p=0
    numDeComandos = int(input())
    histDeComandos = [""]*numDeComandos
    for jnd in range(numDeComandos):
        command = input()
        histDeComandos[jnd] = command
        p = novaPosicao(p, command, histDeComandos)
    print(p)
