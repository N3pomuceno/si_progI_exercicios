#Programa
#Subprograma
def mostrarInverso(vet):
    for ind in range(len(vet)):
        print("N[{}] = {}".format(ind, vet[len(vet) - ind - 1]))
    return None

#Principal
vetor = []
for ind in range(20):
    numero = int(input())
    vetor.append(numero)
mostrarInverso(vetor)
