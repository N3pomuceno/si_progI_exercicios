#Programa
def linhaDeChegada(dis, posts):
    for pos in range(len(postos)-1):
        if (posts[pos+1] - posts[pos]) > dis:
            return "N"
    if dis*(len(postos)+1) < 42195:
        return "N"
    else:
        return "S"


#Principal
numDePostos, distInter = map(int, input().split())
postos = list(map(int, input().split()))

print(linhaDeChegada(distInter, postos))

"""
8 6000
0 6000 12000 18000 24000 32000 37000 40000
"""