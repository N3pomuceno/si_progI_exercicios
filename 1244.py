#Programa
"""
4
Top Coder comp Wedn at midnight
one three five
I love Cpp
sj a sa df r e w f d s a v c x z sd fd
as ae df s a w df aw cv fds

"""

#Subprogramas
def ordenacaoPorTamanho(frs):
    for jnd in range(len(frs)):
    #Para localizar a maior palavra\
        maior = len(frs[jnd])
        maiorpalavra = frs[jnd]
        pos1 = jnd
        neces = False
        for lnd in range(jnd+1, len(frs)):
            if len(frs[lnd]) > maior:
                maior = len(frs[lnd])
                maiorpalavra = frs[lnd]
                pos1 = lnd
                neces = True
    #Para localizar a primeira menor palavra que ele.
        if neces:
            pos2 = primeiroMenor(frs, jnd, maior)
            frs.pop(pos1)
            frs.insert(pos2, maiorpalavra)


    #impressão
    texto = ""
    for jnd in range(len(frase)):
        texto += frase[jnd] + " "
    texto = texto[0:len(texto) - 1]
    print(texto)
    return None

def primeiroMenor(lista, menor, m):
    for nnd in range(menor, len(lista)):
        if len(lista[nnd]) < m:
            return nnd

#Principal
numDeCasos = int(input())

for ind in range(numDeCasos):
    frase = list(input().split())
    ordenacaoPorTamanho(frase)


