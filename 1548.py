#Programa
#Rever aula de ordenação, colocar em ordem, e comparar o original com o ordenado e verificar quantos estão no mesmo lugar.
#Subprograma
def ordenacao(lista):
    ordem = [0]*len(lista)
    for ind in range(len(lista)):
        ordem[ind] = lista[ind]
    for ind in range(len(ordem)):
        maior = ordem[ind]
        pos = ind
        for jnd in range(ind+1, len(ordem)):
            if ordem[jnd] > maior:
                maior = ordem[jnd]
                pos = jnd
        ordem[pos] = ordem[ind]
        ordem[ind] = maior
    contagem = 0
    for ind in range(len(lista)):
        if lista[ind] == ordem[ind]:
            contagem += 1
    print(contagem)
    return None



#principal
numDeCasos = int(input())
for ind in range(numDeCasos):
    numDeAlunos = int(input())
    listaDeNotas = list(map(int, input().split()))
    ordenacao(listaDeNotas)
