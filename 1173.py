# TODO estudar
# Programa

# Subprogramas
def potencia(num, vet):
    if len(vet) == 10:
        return mostra(vet)
    vetor.append(2*num)
    potencia(2*num, vet)
    return None


def mostra(vet):
    for ind in range(len(vet)):
        print("N[{}] = {}".format(ind, vet[ind]))
    return None

# Principal


numero = int(input())
vetor = [numero]
potencia(numero, vetor)
