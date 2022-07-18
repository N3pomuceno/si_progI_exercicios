# Programa
"""
4
1 x 1
2 x 1
2 x 0
2 x 1
1 x 1
2 x 2
3 x 1
3 x 1
"""
# Subprogramas
def resultado(p1t1, p1t2, p2t1, p2t2):
    #Saldo de Gols
    if (p1t1+p2t1) > (p1t2+p2t2):
        return print("Time 1")
    elif (p1t1+p2t1) < (p1t2+p2t2):
        return print("Time 2")
    else:
        if p1t2 < p2t1:
            return print("Time 1")
        elif p1t2 > p2t1:
            return print("Time 2")
        else:
            return print("Penaltis")

    return None

# Principal
numDeJogos = int(input())
for partida in range(numDeJogos):
    golsP1T1, golsP1T2 = map(int, input().split(" x "))
    golsP2T2, golsP2T1 = map(int, input().split(" x "))
    resultado(golsP1T1, golsP1T2, golsP2T1, golsP2T2)


