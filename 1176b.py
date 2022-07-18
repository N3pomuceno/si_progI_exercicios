# TODO estudar
# Programa
# Subprogramas
def fibonacci(num):
    c = 0
    if num == 0:
        return 0
    elif num == 1:
        return 1
    fib2 = 0
    fib1 = 1
    while c != num - 1:
        fib = fib1 + fib2
        fib2 = fib1
        fib1 = fib
        c += 1
    return fib

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
