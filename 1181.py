#Programa
#Subprogramas
def operacao(mat, linha, defin):
    resultado = 0
    if defin == "S":
        for jnd in range(12):
            resultado += mat[linha][jnd]
        print(resultado)
    elif defin == "M":
        for jnd in range(12):
            resultado += mat[linha][jnd]
        resultado /= 12
        print(resultado)
    return None


#Programa
linhaDeOperacao = int(input())
definicaoDeOperacao = input()

#criação de matriz
matriz = []
for coluna in range(12):
    novaLinha = []
    for linha in range(12):
        num = float(input())
        novaLinha.append(num)
    matriz.append(novaLinha)

operacao(matriz, linhaDeOperacao, definicaoDeOperacao)
