#Programa Carneirinhos
#TODO estudar

#Subprograma
'''
Fazendo por isso estava dando time exceeded
def quantidadeDeCarneiros(lista):
    qts = []
    for id in lista:
        if id not in qts:
            qts.append(id)
    print(len(qts))
    return None
'''
def mostrar(ident):
    print(len(set(ident)))
    return None

#Principal
numDeCasos = int(input())
for ind in range(numDeCasos):
    numDeCarneiros = int(input())
    identificador = list(map(int, input().split()))
    mostrar(identificador)
