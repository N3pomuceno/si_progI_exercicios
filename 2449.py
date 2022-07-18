# Programa
#Subprogramas
def limite(temp, num):
    qtd = 0
    for ind in range(len(temp)-1):
        if temp[ind]!= num:
            numero1 = num - temp[ind]
            if numero1 > 0:
                temp[ind] += numero1
                temp[ind+1] += numero1
            elif numero1 < 0:
                temp[ind] += numero1
                temp[ind+1] += numero1
            qtd += abs(numero1)
    return qtd


# Principal
numDePinos, alturaDesb = map(int, input().split())
alturaDosPinos = list(map(int, input().split()))

qtdMinDeMovimento= limite(alturaDosPinos, alturaDesb)
print(qtdMinDeMovimento)

