#Programa
#TODO estudar
#Subprogramas
"""
Com recursividade o time limit fica exceeded o tempo toda hora.

def fibo(num, cont):
    cont[0] += 1
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return fibo(num - 1, cont) + fibo(num - 2, cont)
"""

def fibo(lista):
    for ind in range(2, 41):
        lista.append([lista[ind-1][0]+lista[ind-2][0], lista[ind-1][1] + lista[ind-2][1]+2])
    return None

def localiza(lista, lin, col):
    for ind in range(len(lista)):
        if ind == lin:
            num = lista[ind][col]
    return num

#Principal
resultado = [[0,0],[1,0]]
fibo(resultado)
numDeTestes = int(input())
for ind in range(numDeTestes):
    caso = int(input())
    print("fib({}) = {} calls = {}".format(caso, localiza(resultado, caso, 1), localiza(resultado, caso, 0)))
