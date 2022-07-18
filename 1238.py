#Programa

#Subprogramas
def concatenacao(p1, p2):
    if len(p1) < len(p2):
        menor = "p1"
        menorTamanho = len(p1)
    elif len(p1) > len(p2):
        menor = "p2"
        menorTamanho = len(p2)
    else:
        menor = ""
        menorTamanho = len(p1)
    resultado = ""
    for let in range(menorTamanho):
        resultado += p1[let]
        resultado += p2[let]
    if menor == "p1":
        for resto in range(menorTamanho, len(p2)):
            resultado += p2[resto]
    else:
        for resto in range(menorTamanho, len(p1)):
            resultado += p1[resto]
    print(resultado)
    return None


#Principal
numDeCasos = int(input())
for caso in range(numDeCasos):
    part1, part2 = map(str, input().split())
    concatenacao(part1, part2)
