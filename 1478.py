# TODO estudar
#Programa


#Subprogramas
def matriz(num):
    mat = []
    for ind in range(num):
        newLine = []
        for jnd in range(num):
            pos = abs(ind - jnd) + 1
            newLine.append(pos)
        mat.append(newLine)
    mostrar(mat)
    print()
    return None

def mostrar(mat):
    for linha in mat:
        print('   '.join(map(str, linha)))
    return None

#https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row


#Principal
numero = int(input())
while numero != 0:
    matriz(numero)
    numero = int(input())
