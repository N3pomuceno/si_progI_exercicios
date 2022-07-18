# Programa
# Subprogramas
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

def mostrar(lista):
    for linha in lista:
        print("Fib({}) = {}".format(linha[0], linha[1]))


#Principal
lista = []
numDeCasos = int(input())
for ind in range(numDeCasos):
    numero = int(input())
    lista.append([numero, fibonacci(numero)])
mostrar(lista)
