#Programa
#Subprograma
def criacaoDeVetor(numero,vetor):
    for num in range(1,numero+1):
        if numero % num == 0:
            vetor.append(num)
    impressao(vetor)
    return None

def impressao(vet):
    for ind in range(len(vet)):
        print(vet[ind])
    return None

#Principal
num = int(input())
divisores = []
criacaoDeVetor(num, divisores)
