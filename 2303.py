#Programa


#Subprogramas
def melhorLote(colheita, lin, col):
    #Definindo o valor inicial para comparação entre lotes é por palpite inicialmente nulo
    maiorValorPorLote = 0

    #Na sequência tem o algoritmo que calcula os valores por lote.
    #Os dois while's são para definir o limite da colheita e de conseguir endereçar lote a lote.
    linha = 0
    while linha < len(colheita):
        coluna = 0
        while coluna < len(colheita[0]):
            valorPorLote = 0

            #Os dois for's são para calcular o valor que o lote produz, que tbm depende dos valores dos while's.
            for ind in range(lin):
                for jnd in range(col):
                    valorPorLote += colheita[linha+ind][coluna+jnd]

            #Comparação dos valores de cada um dos lotes e caso seu valor seja maior, o valor da variável é substituído.
            if valorPorLote > maiorValorPorLote:
                maiorValorPorLote = valorPorLote
            coluna += col
        linha += lin

    #Impressão do valor.
    print(maiorValorPorLote)
    return None

#Principal
#entrada de quatro valores: Linha, Coluna, LinhaDoLote, ColumaDoLote
lin, col, linLote, colLote = map(int, input().split())

#valores de cada um dos espaços da colheita
valoresDaColheita = []
for ind in range(lin):
    novaLinha = []
    novaLinha = list(map(int, input().split()))
    valoresDaColheita.append(novaLinha)

#Definido então qual é o melhor lote!
#chamando uma função
melhorLote(valoresDaColheita, linLote, colLote)
