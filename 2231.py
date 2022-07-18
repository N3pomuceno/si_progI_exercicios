#Programa

#Subprogramas
def comparacao(orig, acum, inter, c):
    #Calculando médias com a ideia da subtração do maior valor e menor valor do intervalo e dividir pela intervalo.
    medias = []
    for ind in range(len(orig) - inter + 1):
        num = (acum[ind+inter]-acum[ind])/inter
        medias.append(num)

    #Deinição de qual é a maior e menor média através da lista de médias.
    maior = menor = medias[0]
    for media in medias:
        if media > maior:
            maior = media
        elif media < menor:
            menor = media

    #função de impressão
    mostrar(maior, menor, c)
    return None

def mostrar(M, m, c):
    print("Teste {}".format(c))
    print("%d %d"%(m, M))
    print()
    return None

#Principal

#Contagem para lembrar a quantidade de testes sendo feita.
contagem= 1

#Input de entrada para definir quantidade de temperaturas e os intervalos que terão que ser calculados.
totalTemp, tamDoInt = map(int, input().split())

#While que define que continuará fazendo testes até ambas as entradas iniciais serem nulas. (não vi o caso se somente uma delas forem nula.)
while totalTemp != 0 and tamDoInt != 0:

    #Definindo valores das listas, normal e acumulada.
    listaOrig = [0]*(totalTemp)
    listaAcum = [0]*(totalTemp + 1)
    for ind in range(totalTemp):
        listaOrig[ind] = int(input())
        listaAcum[ind+1] = listaAcum[ind] + listaOrig[ind]

    #Função que faz a comparação e retorna a menor e maior média respectivamente.
    comparacao(listaOrig, listaAcum, tamDoInt, contagem)

    contagem += 1
    totalTemp, tamDoInt = map(int, input().split())

