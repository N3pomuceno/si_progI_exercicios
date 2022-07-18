"""

regra do jogo:
queremos o esforço de cada uma das trilhas, seja de ida ou seja de volta, onde esse esforço só é contado quando subimos
não quando descemos. Então basta fazer a diferença do próximo ponto com o atual, se for maior que zero, pf - pi > 0
aí sim se soma ao esforço.
Se dois esforços forem iguais, basta pegar o índice da trilha menor.

5 - número de trilhas

Próximas linhas: Primeiro número de intervalo iguais na trilha, os próximos pontos são altura de cada um dos pontos
4 498 500 498 498

10 60 60 70 70 70 70 80 90 90 100

5 200 190 180 170 160

2 1000 900

4 20 20 20 20

"""

# TODO Terminar esse código
#Programa

#Subprogramas
def trilhaDeMenorEsforço(num, alts, lista):
    resultado1 = 0
    resultado2 = 0
    for ind in range(num - 1):
        if

        elif
    if

    else:

        return lista


def comparacao(lista):
    pos = 0
    for ind in range(len(lista)):
        if lista[ind] < lista[pos]:
            pos = ind
    return pos



#Principal
#Número de trilhas inicialmente definidos.
numeroDeTrilhas = int(input())
esforçoPorTrilha = []
for ind in range(numeroDeTrilhas):
    info = list(map(int, input().split()))
    numeroDeIntervalos = info[0]
    alturas = info[1:]
    esforçoPorTrilha = trilhaDeMenorEsforço(numeroDeIntervalos, alturas, esforçoPorTrilha)
melhorTrilha = comparacao(esforçoPorTrilha)

