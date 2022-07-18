# Programa


#Subprogramas
def sorteio(ordem):
    for ind in range(len(ordemDeEntrada)):
        if (ind+1) == ordemDeEntrada[ind]:
            print("Teste {}".format(contagem))
            print(ind+1)
            print()
            return None
    return None
#Principal

contagem = 1
qtdDePessoas = int(input())
while qtdDePessoas != 0:
    ordemDeEntrada = list(map(int, input().split()))
    sorteio(ordemDeEntrada)

    contagem +=1
    qtdDePessoas = int(input())
