#Programa Subsequências


#Subprogramas
def subseq(caso, sub):
    if len(caso) < len(sub):
        print("No")
        return None
    else:
        ondeParou = 0
        for jnd in range(len(sub)):
            if sub[jnd] not in caso[ondeParou:]:
                print("No")
                return None
            else:
                ondeParou = ondeEstaALetra(sub[jnd], caso, ondeParou)
        print("Yes")
        return None

def ondeEstaALetra(letra, palavra, lugar):
    for posicao in range(lugar, len(palavra)):
        if palavra[posicao] == letra:
            pos = posicao
            return pos+1


#Principal
numDeCasosTeste = int(input())

for ind in range(numDeCasosTeste):
    caso = input()
    numDeQueries = int(input())
    for q in range(numDeQueries):
        querie = input()
        subseq(caso, querie)

