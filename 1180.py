#Programa

#Subprograma
def menorPosicao(vet):
    pos = 0
    for ind in range(len(vet)):
        if vet[ind] < vet[pos]:
            pos = ind
    return pos

def mostreme(val, pos):
    print("Menor valor: {}".format(val))
    print("Posicao: {}".format(pos))
    return None

#Principal

tamanho = int(input())
vetor = list(map(int, input().split()))
posicao = menorPosicao(vetor)
menorValor = vetor[posicao]
mostreme(menorValor, posicao)
