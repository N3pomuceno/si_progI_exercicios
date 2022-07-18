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
    return None

def mostrar(mat):
    for linha in range(len(mat)):
        line = ""
        for coluna in range(len(mat)):
            line += " %3d" %mat[linha][coluna]
        print(line[1:])
    print()
    return None


#Principal
numero = int(input())
while numero != 0:
    matriz(numero)
    numero = int(input())
