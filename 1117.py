#Programa
#Subprograma
def calculoDeMedias(nota, lista):
    lista.append(nota)
    if len(lista) == 2:
        media = lista[0] + lista[1]
        media /= 2
        mostrar(media)
    return None

def mostrar(notafinal):
    print("media = {}".format(notafinal))
    return None

#Principal
listaDeNotas = []
for numDeNotas in range(2):
    novaNota = float(input())
    while novaNota < 0 or novaNota > 10:
        print("nota invalida")
        novaNota = float(input())
    calculoDeMedias(novaNota, listaDeNotas)
