#Programa


#Principal
numDeCoposQuebrados = 0
numDeCasos = int(input())

for ind in range(numDeCasos):
    latas, copos = map(int, input().split())
    if latas > copos:
        numDeCoposQuebrados += copos

print(numDeCoposQuebrados)
