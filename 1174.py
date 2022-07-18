#Programa
#Subprogramas
def mostraDeSelecao(vet):
    for ind in range(len(vet)):
        if vet[ind] <= 10:
            print("A[{}] = {:.1f}".format(ind, vet[ind]))
    return None

#Principal
vetorDeCem = []
for ind in range(100):
    numero = float(input())
    vetorDeCem.append(numero)
mostraDeSelecao(vetorDeCem)
