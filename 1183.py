#Programa
#Subprogramas
def operacao(mat, defin):
    resultado = 0
    if defin == "S":
        for linha in range(len(mat)):
            for coluna in range(len(mat)):
                if coluna > linha:
                    resultado += mat[linha][coluna]
        print("{:.1f}".format(resultado))
    elif defin == "M":
        c = 0
        for linha in range(len(mat)):
            for coluna in range(len(mat)):
                if coluna > linha:
                    c += 1
                    resultado += mat[linha][coluna]
        resultado /= c
        print("{:.1f}".format(resultado))
    return None


#Programa
definicaoDeOperacao = input()

#criação de matriz
matriz = []
for linha in range(12):
    novaLinha = []
    for coluna in range(12):
        num = float(input())
        novaLinha.append(num)
    matriz.append(novaLinha)

operacao(matriz, definicaoDeOperacao)
