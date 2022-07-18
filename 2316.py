#Programa - Autorama
"""
3 3 6
3 1
1 1
2 1
3 2
3 3
2 2

2 2 5
2 1
2 1
1 1
2 1
1 2

4 4 21
3 1
2 1
4 2
4 3
4 4
4 1
1 1
1 2
1 3
3 2
3 3
2 2
2 3
3 4
2 4
3 1
1 4
2 1
4 3
2 2
3 2
"""
#Subprogramas
def atualizacaoDoSensor(carPS, car, post):
    #Localiza o carrinho e verifica se ele está pulando sensor ou não, caso negativo, some mais um ao sensor. Reinicie seu desempate.
    pos = localiza(carPS, car)
    if carPS[pos][1] == post-1:
        carPS[pos][1] += 1
        carPS[pos][3] = 0
        #Verificação de se tem algum outro carrinho que já passou pelo sensor do carrinho atual. Caso positivo, some mais um ao critério de desempate dos outros carrinhos
        #Essa soma no desempate, será o critério na ordenação no final.
        for ind in range(len(carPS)):
            if carPS[ind][1] == carPS[pos][1] and carPS[ind][3] == carPS[pos][3] and ind != pos:
                carPS[ind][3] += 1

    #Caso o carrinho chegue no último sensor, ele reinicia a contagem de sensores e aumenta seu número de voltas!
    if carPS[pos][1] == 4:
        carPS[pos][1] = 0
        carPS[pos][2] += 1
    return None

def localiza (lista, num):
    for ind in range(len(lista)):
        if lista[ind][0] == num:
            return ind

# PRINCIPAL
# Entradas
numDePostosDeChecagem, numDeCarrinhos, numDeLeituras = map(int, input().split())
# (indice + 1) equivale ao carrinho

carrinhoSensColoc = [0]*numDeCarrinhos
for ind in range(numDeCarrinhos):
    carrinhoSensColoc[ind] = [ind+1, 0, 0, 0] # 4 colunas: identificação de carro, endereço do sensor atual, quantidade de voltas, desempate

for leitura in range(numDeLeituras):
    carrinho, posto = map(int, input().split())

    # Atualização da leitura dada pelos sensores, segunda coluna. E depois atualização de colocação, terceira coluna
    atualizacaoDoSensor(carrinhoSensColoc, carrinho, posto)


#Ordem de chegada! Ordenação decrescente da relação entre os valores. Do maior, primeira posição, para o menor, última posição
# A ideia de ver quem é o maior é a quantidade de sensores que o carrinho passou, ou seja: número do sensor atual + o produto da quantidade de voltas dadas pelo numDeSensores
for ind in range(numDeCarrinhos):
    posMaior = ind
    for jnd in range(ind+1, numDeCarrinhos):
        if carrinhoSensColoc[jnd][1] + carrinhoSensColoc[jnd][2] * numDePostosDeChecagem > carrinhoSensColoc[posMaior][1] + carrinhoSensColoc[posMaior][2]*numDePostosDeChecagem:
            posMaior = jnd

        #critério de desempate
        if carrinhoSensColoc[jnd][1] + carrinhoSensColoc[jnd][2] * numDePostosDeChecagem == carrinhoSensColoc[posMaior][1] + carrinhoSensColoc[posMaior][2]*numDePostosDeChecagem:
            #Checar posição de acordo com o desempate.
            if carrinhoSensColoc[jnd][3] > carrinhoSensColoc[posMaior][3]:
                posMaior = jnd
    #Troca de posição da lista
    temp = carrinhoSensColoc[posMaior]
    carrinhoSensColoc[posMaior] = carrinhoSensColoc[ind]
    carrinhoSensColoc[ind] = temp

#print(carrinhoSensColoc) para verificar se ocorreu tudo certo.

#impressão
for pos in range(numDeCarrinhos):
    print("{} ".format(carrinhoSensColoc[pos][0]), end="")

#Outra forma de impressão.
#ordemDeChegada = ""
#for pos in range(numDeCarrinhos):
    #ordemDeChegada += str(carrinhoPorSensorPorColocacao[pos][0])
    #if pos != numDeCarrinhos-1:
    #    ordemDeChegada += " "
#print(ordemDeChegada)

