#programa

#Subprogramas
def duelo(nmPar, nmImpar):
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print(nmPar)
    else:
        print(nmImpar)
    return None

#principais
numDeInterações = int(input())
c = 0 #Contagem
while numDeInterações != 0:
    nome1 = input()  # Associado com o par
    nome2 = input()  # Associado com o impar
    c += 1
    print("Teste {}".format(c))
    for ind in range(numDeInterações):
        duelo(nome1, nome2)
    print()
    numDeInterações = int(input())
