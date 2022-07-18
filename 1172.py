#Programa

#Subprogramas
def revisaoDeNegativo(vet):
    for ind in range(len(vet)):
        if vet[ind] <= 0:
            vet[ind] = 1
    return None

def mostrar(vet):
    for ind in range(len(vet)):
        print("X[{}] = {}".format(ind,vet[ind]))
    return None


#Principal
vetor = []
for ind in range(10):
    numero = int(input())
    vetor.append(numero)
revisaoDeNegativo(vetor)
mostrar(vetor)
