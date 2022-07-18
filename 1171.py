# Programa
#Subprograma
def listaDeRepeticao(num, lista):
    if novoNum(num, lista):
        lista.append([num,1])
    else:
        for linha in lista:
            if num == linha[0]:
                linha[1] += 1
    return None

def novoNum(num ,lista):
    for linha in lista:
        if num == linha[0]:
            return False
    return True

def ordenacao(lista):
    def menor(ind, totalNum, lista):
        pos = ind
        for jnd in range(ind, totalNum):
            if lista[jnd][0] < lista[pos][0]:
                pos = jnd
        return pos

    for ind in range(len(lista)):
        menorPosicao = menor(ind, len(lista), lista)
        if menorPosicao != ind:
            temp1 = lista[menorPosicao][0]
            lista[menorPosicao][0] = lista[ind][0]
            lista[ind][0] = temp1
            temp2 = lista[menorPosicao][1]
            lista[menorPosicao][1] = lista[ind][1]
            lista[ind][1] = temp2
    return None

def mostrar(lista):
    for ind in range(len(lista)):
        print("{} aparece {} vez(es)".format(lista[ind][0], lista[ind][1]))
    return None


#Principal
numDeEntradas = int(input())
listaDeValores = []
for ind in range(numDeEntradas):
    numero = int(input())
    listaDeRepeticao(numero, listaDeValores)
ordenacao(listaDeValores)
mostrar(listaDeValores)
