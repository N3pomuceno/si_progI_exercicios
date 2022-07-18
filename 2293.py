#Programa
#Soma de linhas e colunas!
"""
3 4
81 28 240 10
40 10 100 240
20 180 110 35

"""
#Principal

linhas, colunas = map(int, input().split())
totalDeContas = [0]*(linhas+colunas)

#Montando matriz.podia ser uma função
matriz = []
for linha in range(linhas):
    novaLinha = list(map(int, input().split()))
    matriz.append(novaLinha)

#Cálculo das somas. Podia ser uma função
for ind in range(linhas):
    for jnd in range(colunas):
        totalDeContas[ind] += matriz[ind][jnd]

for knd in range(ind+1, colunas + ind+1):
    for lnd in range(linhas):
        totalDeContas[knd] += matriz[lnd][knd-ind-1]

#Comparação com o maior.podia ser uma função
maior= totalDeContas[0]
for soma in totalDeContas[1:]:
    if soma > maior:
        maior = soma

#Impressão
print(maior)



