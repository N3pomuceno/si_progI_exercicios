#Programa


#Subprogramas
def calculoDeImg(plant, lin, col):
    imagemIntegral = [None]*(lin+1)
    for ind in range(lin+1):
        imagemIntegral[ind] = [0]*(col+1)

    for ind in range(1, lin+1):
        for jnd in range(1, col+1):
            imagemIntegral[ind][jnd] = imagemIntegral[ind-1][jnd] + imagemIntegral[ind][jnd-1] + plant[ind-1][jnd-1] - imagemIntegral[ind-1][jnd-1]

    return imagemIntegral


def colheitaPorLote(img, linL, colL):
    maior = 0
    for ind in range(len(img) - linL):
        for jnd in range(len(img[0]) - colL):
            valorLote = img[ind][jnd] - img[ind+linL][jnd] - img[ind][jnd+colL] + img[ind+linL][jnd+colL]
            if valorLote > maior:
                maior = valorLote
    print(maior)
    return None

#Principal

#entrada de dimensões da colheita e dos lotes que queremos verificar.
linha, coluna, linLote, conLote = map(int, input().split())

#Matriz dos números da plantação
plantacao = [None]*linha
for ind in range(linha):
    novaLinha = list(map(int, input().split()))
    plantacao[ind] = novaLinha

#Imagem integral da matriz de plantação.
imgIntegral = calculoDeImg(plantacao, linha, coluna)


#Maior colheita por lote e impressão da maior colheita.
colheitaPorLote(imgIntegral, linLote, conLote)
