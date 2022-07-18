#Programa

#Subprograma
def preencher(num, par, imp, rep):
    if num % 2 == 0:
        par.append(num)
        if len(par) == 5:
            nome = "par"
            mostrar(nome, par)
    elif num % 2 != 0:
        imp.append(num)
        if len(imp) == 5:
            nome = "impar"
            mostrar(nome, imp)

    if rep == 14:
        nome = "impar"
        mostrar2(nome, imp)
        nome = "par"
        mostrar2(nome, par)
    return None

def mostrar(texto, lista):
    for ind in range(5):
        print("{}[{}] = {}".format(texto, ind, lista[ind]))
    return None

def mostrar2(texto, lista):
    for ind in range(len(lista) - 5):
        print("{}[{}] = {}".format(texto, ind, lista[ind + 5]))
    return None


#Principal
par = []
impar = []
for ind in range(15):
    numero = int(input())
    preencher(numero, par, impar, ind)
